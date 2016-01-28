# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder, Servo, Color, DigitalInput

from control.long_range_ir import LRIR
from control.Wall_Follow import WallFollow

from modules import *
from constants import *

#TODO: Get rid of excess timers

class Robot(SyncedSketch):

    def setup(self):
        ####################
        ####  EE SETUP  ####
        ####################

        # Motor object representing the left motor.
        self.leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        # Encoder object for the left motor.
        self.leftEncoder = Encoder(self.tamp, LEFT_DRIVE_ENCODER_YELLOW, LEFT_DRIVE_ENCODER_WHITE)
        # Motor object representing the right motor.
        self.rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        # Encoder object for the right motor.
        self.rightEncoder = Encoder(self.tamp, RIGHT_DRIVE_ENCODER_YELLOW, RIGHT_DRIVE_ENCODER_WHITE)

        # Motor object representing the intake mechanism motors.
        self.intakeMotor = Motor(self.tamp, HUGS_MOTOR_CONTROLLER_DIRECTION, HUGS_MOTOR_CONTROLLER_PWM)
        # Encoder object for the intake motor.
        self.intakeEncoder = Encoder(self.tamp, HUGS_MOTOR_ENCODER_YELLOW, HUGS_MOTOR_ENCODER_WHITE)

        # Motor object representing the conveyor belt motor.
        self.conveyorMotor = Motor(self.tamp, BELT_MOTOR_CONTROLLER_DIRECTION, BELT_MOTOR_CONTROLLER_PWM)
        # Encoder object for the conveyor belt motor.
        self.conveyorEncoder = Encoder(self.tamp, BELT_MOTOR_ENCODER_YELLOW, BELT_MOTOR_ENCODER_WHITE)

        # Long range IR sensors
        self.irBL = LRIR(self.tamp, LONG_DISTANCE_IR_BL)
        self.irBR = LRIR(self.tamp, LONG_DISTANCE_IR_BR)
        self.irFL = LRIR(self.tamp, LONG_DISTANCE_IR_FL)
        self.irFR = LRIR(self.tamp, LONG_DISTANCE_IR_FR)

        # Color sensor
        self.color = Color(self.tamp)

        # Limit switches
        self.conveyorLimSwitch = DigitalInput(self.tamp, CONVEYOR_LIMIT_SWITCH)
        self.blockLimSwitch = DigitalInput(self.tamp, BLOCK_LIMIT_SWITCH)

        # Servo controlling the door of the collection chamber.
        self.backDoorServo = Servo(self.tamp, SERVO_PIN)
        # Make sure the door is closed
        self.backDoorServo.write(SERVO_CLOSE)

        # The switch that tells the program that the competition has started
        self.competitionModeSwitch = DigitalInput(self.tamp, COMPETITION_MODE)

        #################################
        ####  INTERNAL MODULE SETUP  ####
        #################################

        # Timer object to moderate checking for intake errors.
        self.intakeTimer = Timer()
        # Are the intake motors reversing? True if so, False if going forwards.
        self.intakeDirection = False
        # Start the intake motor.
        self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)

        # Wall Follow object
        self.wallFollow = WallFollow(self.leftMotor, self.rightMotor, Timer(), self.irFL, self.irFR, self.irBL, self.irBR)

        # A timer to make sure timesteps are only 10 times/second
        self.timestepTimer = Timer()
        # Timer object describing how long the current module has been running.
        self.moduleTimer = Timer()
        # Timer for the whole game
        self.gameTimer = Timer()

        # Runs the PICKUP process
        self.pickup = PickupModule(self.moduleTimer, self.conveyorLimSwitch, self.conveyorMotor, self.conveyorEncoder)
        # Runs the DROPOFF process
        self.dropoff = DropoffModule(self.moduleTimer, self.backDoorServo, self.rightMotor, self.leftMotor, self.rightEncoder)
        # Runs the FOLLOW process TODO: Fix forward to actually mean forward.
        self.follow = FollowModule(self.moduleTimer, self.leftMotor, self.rightMotor, self.intakeMotor, self.wallFollow, FORWARD_SPEED, self.blockLimSwitch)
        # Runs the CHECK process. TODO: pass in proper timers.
        self.check = CheckModule(self.moduleTimer, self.leftMotor, self.rightMotor, self.intakeMotor, self.color)
        # Waits for the game to start
        self.off = OffModule(self.gameTimer, self.competitionModeSwitch)

        # Describes which stage of the program is running.
        self.module = MODULE_OFF

    def loop(self):
        if self.timestepTimer.millis() > 100:
            self.timestepTimer.reset()
            #print "Module Number", self.module

            state = -1
            if self.module == MODULE_OFF:
                state = self.off.run()
            elif self.module == MODULE_CHECK:
                state = self.check.run()
            elif self.module == MODULE_PICKUP:
                state = self.pickup.run()
            elif self.module == MODULE_DROPOFF:
                state = self.dropoff.run()
            elif self.module == MODULE_FOLLOW:
                state = self.follow.run()
            else:
                print "Attempting to run nonexistent module"
                self.stop()

            self.updateState(state)

        if self.gameTimer.millis() > GAME_LENGTH:
            self.module = MODULE_END
            self.backDoorServo.write(SERVO_OPEN)
            self.stop()
            return

    ## Switch module if necessary.
    def updateState(self, module):
        if self.module == module:
            return
        elif module == MODULE_OFF:
            self.off.start()
            self.module = MODULE_OFF
            return
        elif module == MODULE_CHECK:
            self.check.start()
            self.module = MODULE_CHECK
            return
        elif module == MODULE_PICKUP:
            self.pickup.start()
            self.module = MODULE_PICKUP
            return
        elif module == MODULE_DROPOFF:
            self.dropoff.start()
            self.module = MODULE_DROPOFF
            return
        elif module == MODULE_FOLLOW:
            self.follow.start()
            self.module = MODULE_FOLLOW
            return
        else:
            print "Attempting to switch to nonexistent module"
            self.stop()

    ## Make sure that the intake motor does not stall.
    #  If so, reverse the intake motors.
    #
    # @param checkTime  Time in ms between checking stalls.
    # @param reverseTime    Time in ms that the intake motors will reverse if needed.
    def checkForIntakeErrors(self, checkTime = 100, reverseTime = 800):

        if self.intakeDirection:    # We are moving forward.
            if self.intakeTimer.millis() > checkTime:
                self.intakeTimer.reset()
                if self.intakeEncoder.val < INTAKE_ENCODER_LIMIT: # if we're stalled
                    self.intakeDirection = True
                    self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)
                else: # if we're not stalled
                    self.intakeEncoder.write(0)

        else:                       # We are reversing the motors.
            if self.intakeTimer.millis() > reverseTime:
                self.intakeTimer.reset()
                self.intakeDirection = False
                self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)
                self.intakeEncoder.write(0)

        self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()