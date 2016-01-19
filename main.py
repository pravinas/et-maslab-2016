# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder, Servo

from find import FindModule
from pickup import PickupModule
from dropoff import DropoffModule

from constants import *

class Robot(SyncedSketch):

    def setup(self):

        # The color of block we care about. Should be RED or GREEN
        self.blockColor = RED   # TODO: Check which color we care about.

        # TODO: Figure out which pins are hooked up where.
        # Motor object representing the left motor.
        self.leftMotor = Motor(self.tamp, 1, 2)
        # Encoder object for the left motor.
        self.leftEncoder = Encoder(self.tamp, 3, 4)
        # Motor object representing the right motor.
        self.rightMotor = Motor(self.tamp, 5, 6)
        # Encoder object for the right motor.
        self.rightEncoder = Encoder(self.tamp, 7, 8)

        # Motor object representing the intake mechanism motors.
        self.intakeMotor = Motor(self.tamp, 9, 10)
        # Encoder object for the intake motor.
        self.intakeEncoder = Encoder(self.tamp, 11, 12)
        # The limit point at which the motor is considered stalled.
        self.intakeEncoderLimit = 150
        # The speed of the intake motors.
        self.intakePower = 150
        # Timer object to moderate checking for intake errors.
        self.intakeTimer = Timer()
        # Are the intake motors going forward? True if so, False if reversing.
        self.intakeDirection = True

        # Motor object representing the conveyor belt motor.
        self.conveyorMotor = Motor(self.tamp, 13, 14)
        # Encoder object for the conveyor belt motor.
        self.conveyorEncoder = Encoder(self.tamp, 15, 16)
        # The encoder count for as far as we want the encoder to move.
        self.conveyorEncoderLimit = 5 * 3200
        # The speed of the conveyor belt. (0-255)
        self.conveyorPower = 130

        # Servo controlling the door of the collection chamber.
        self.backDoorServo = Servo(self.tamp, 17)

        # Start the intake motor.
        self.intakeMotor.write(self.intakeDirection, self.intakePower)

        # Timer object describing how long the current module has been running.
        self.moduleTimer = Timer()
        # Runs the FIND process
        self.find = FindModule(self.moduleTimer, self.leftMotor, self.rightMotor, self.blockColor)
        # Runs the PICKUP process
        self.pickup = PickupModule(self.moduleTimer)
        # Runs the DROPOFF process
        self.dropoff = DropoffModule(self.moduleTimer, self.backDoorServo)
        # Describes which stage of the program is running.
        self.module = MODULE_FIND

        self.checkForInitializationErrors()

    def loop(self):

        self.updateState(self.module.run())

        # Passive processes go here.
        self.checkForIntakeErrors()

    ## TODO: Documentation
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
            self.module = MODULE_PICKUP
            return


    ## Make sure that the intake motor does not stall.
    #  If so, reverse the intake motors.
    #
    # @param checkTime  Time in ms between checking stalls.
    # @param reverseTime    Time in ms that the intake motors will reverse if needed.
    def checkForIntakeErrors(self, checkTime = 100, reverseTime = 2000):

        if self.intakeDirection:    # We are moving forward.
            if self.intakeTimer.millis() > checkTime:
                self.intakeTimer.reset()
                if self.intakeEncoder.val < self.intakeEncoderLimit: # if we're stalled
                    self.intakeDirection = False
                    self.intakeMotor.write(self.intakeDirection, self.intakePower)
                else: # if we're not stalled
                    self.intakeEncoder.write(0)

        else:                       # We are reversing the motors.
            if self.intakeTimer.millis() > reverseTime:
                self.intakeTimer.reset()
                self.intakeDirection = True
                self.intakeMotor.write(self.intakeDirection, self.intakePower)
                self.intakeEncoder.write(0)

        self.intakeMotor.write(self.intakeDirection, self.intakePower)

    ## Checks if all initialization processes went smoothly.
    def checkForInitializationErrors(self):
        assert not self.find.checkForInitializationErrors()
        assert not self.pickup.checkForInitializationErrors()
        assert not self.dropoff.checkForInitializationErrors()

    ## Check what color a freshly caught block is.
    #
    # @return 0 if the color sensor does not see a block.
    #         1 if the color sensor sees our color of block
    #         2 if the color sensor sees not our color of block.
    def checkForBlock(self):
        # TODO
        raise NotImplementedError

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()