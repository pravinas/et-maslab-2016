# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder, Servo, Color

from vision import Vision
from logic import Logic
from control.long_range_ir import LRIR

from modules import *
from constants import *

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

        # Servo controlling the door of the collection chamber.
        self.backDoorServo = Servo(self.tamp, SERVO_PIN)
        self.backDoorDervo.write(172)

        #################################
        ####  INTERNAL MODULE SETUP  ####
        #################################

        # Timer object to moderate checking for intake errors.
        self.intakeTimer = Timer()
        # Are the intake motors reversing? True if so, False if going forwards.
        self.intakeDirection = False
        # Start the intake motor.
        #self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)

        # Logic object for FIND module
        self.logic = Logic(self.color, self.leftEncoder, self.rightEncoder)
        # Vision object for FIND module
        self.vision = Vision(RED, CAMERA_WIDTH, CAMERA_HEIGHT)

        # Timer object describing how long the current module has been running.
        self.moduleTimer = Timer()
        # Runs the FIND process
        self.find = FindModule(self.moduleTimer, self.leftMotor, self.rightMotor, self.vision, self.logic)
        # Runs the PICKUP process
        self.pickup = PickupModule(self.moduleTimer, self.conveyorMotor, self.conveyorEncoder)
        # Runs the DROPOFF process
        self.dropoff = DropoffModule(self.moduleTimer, self.backDoorServo)
        # Runs the FOLLOW process TODO: Fix forward to actually mean forward.
        self.follow = FollowModule(self.moduleTimer, self.leftMotor, self.rightMotor, 
                                   self.irBL, self.irBR, self.irFL, self.irFR, 
                                   self.logic, forwardSpeed=-50)
        # Describes which stage of the program is running.
        self.module = MODULE_FIND

        #self.checkForInitializationErrors()

    def loop(self):

        self.updateState(self.module.run())

        # Passive processes go here.
        self.checkForIntakeErrors()

    ## Switch module if necessary.
    def updateState(self, module):
        if self.module == module:
            return
        if module == MODULE_FIND:
            find.start()
            self.module = MODULE_FIND
            return
        if module == MODULE_PICKUP:
            pickup.start()
            self.module = MODULE_PICKUP
            return
        if module == MODULE_DROPOFF:
            dropoff.start()
            self.module = MODULE_PICKUP
            return
        if module == MODULE_FOLLOW:
            follow.start()
            self.module = MODULE_FOLLOW
            return

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

    ## Checks if all initialization processes went smoothly.
    def checkForInitializationErrors(self):
        assert not self.find.checkForInitializationErrors()
        assert not self.pickup.checkForInitializationErrors()
        assert not self.dropoff.checkForInitializationErrors()
        assert not self.follow.checkForInitializationErrors()

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()