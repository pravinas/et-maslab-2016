# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder
from vision import Vision
from logic import Logic
from control import GoStraight

# List of Modules/States. Put any info that needs to persist within the state here.
MODULE_FIND     = {"name": "FIND"   , "timeout": 7000, "target": None, "updateTime": 0}
MODULE_PICKUP   = {"name": "PICKUP" , "timeout": 7000}
MODULE_DROPOFF  = {"name": "DROPOFF", "timeout": 7000}

RED = True
GREEN = not RED

FORWARD = 1
BACKWARD = 0

class Robot(SyncedSketch):

    def setup(self):
        # Describes which stage of the program is running.
        self.module = MODULE_FIND
        # Timer object describing how long the current module has been running.
        self.moduleTimer = Timer()

        # The color of block we care about. Should be RED or GREEN
        self.blockColor = RED   # TODO: Check which color we care about.

        # Vision object to read data from the camera.
        self.vision = Vision(self.blockColor)
        # Timer object describing how much time has passed since the last 
        # camera input was processed.
        self.cameraTimer = Timer()
        # Time in milliseconds between pictures being taken.
        self.cameraTimeout = 500

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

        # Motor object representing the conveyor belt motor.
        self.conveyorMotor = Motor(self.tamp, 13, 14)
        # Encoder object for the conveyor belt motor.
        self.conveyorEncoder = Encoder(self.tamp, 15, 16)
        # The encoder count for as far as we want the encoder to move.
        self.conveyorEncoderLimit = 5 * 3200
        # The speed of the conveyor belt. (0-255)
        self.conveyorPower = 80

        # GoStraight object to control movement
        self.movement = GoStraight(self.leftMotor, self.rightMotor, Timer())
        # Logic processor for sensor inputs.
        self.logic = Logic()

        # Start the intake motor.
        intakePower = 150
        intakeDirection = 1
        self.intakeMotor.write(intakePower, intakeDirection)

        self.checkForInitializationErrors()

    def loop(self):

        if (self.module == MODULE_FIND):
            self.runFindModule()

        elif (self.module == MODULE_PICKUP):
            self.runPickupModule()

        elif (self.module == MODULE_DROPOFF):
            # TODO
            pass

        else:
            print "Unexpected module number:", self.module
            raise Exception()

        # TODO: Passive processes, such as intake motors and interrupts.

    ## Set up the beginning of the find process.
    def startFindModule(self):
        self.module = MODULE_FIND
        self.module["target"] = None
        self.module["updateTime"] = 0
        self.moduleTimer.reset()

    ## Try to find and move towards blocks on the map.
    # 
    # Turn until color is detected.
    # Drive towards largest color until it is centered on the screen.
    def runFindModule(self):
        assert MODULE_FIND == self.module
        target = self.module["target"]

        # Check if we need to exit the module.
        if self.checkForBlock() > 0 or self.moduleTimer.millis() > self.module["timeout"]:
            print "Going from FIND to PICKUP"
            self.startPickupModule()
            return

        ## Capture an image from the camera every so often
        if self.cameraTimer.millis() > self.cameraTimeout:
            self.cameraTimer.reset()

            target = self.module["target"] = self.logic.findTarget(*self.vision.processImage())
            self.module["updateTime"] = self.moduleTimer.millis()

        # Check if we see anything of interest on the screen.
        if target == None:
            arbitraryTarget = 60
            self.movement.move_to_target(arbitraryTarget)
            # TODO: Make sure not to enter this subroutine when there is a block in the blind spot.
        else:
            self.movement.move_to_target(target)
            self.logic.bayesianTargetUpdate(target, self.moduleTimer.millis() - self.module["updateTime"])

    ## Set up the beginning of the pickup process.
    def startPickupModule(self):
        self.module = MODULE_PICKUP
        self.conveyorEncoder.write(0)
        self.conveyorMotor.write(FORWARD, self.conveyorPower)
        self.moduleTimer.reset()

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    def runPickupModule(self):
        assert MODULE_PICKUP == self.module

        # Allow timeout.
        if self.moduleTimer.millis() > self.module["timeout"]:
            print "Timed out from PICKUP to FIND"
            self.startFindModule()
            return

        encval = self.conveyorEncoder.val

        # Move up the conveyor belt until it hits the encoder limit.
        if encval > self.conveyorEncoderLimit:
            self.conveyorMotor.write(BACKWARD, self.conveyorPower)

        # Stop the motor when it gets to the bottom.
        if encval < 0 and self.moduleTimer.millis() > 200:
            self.conveyorMotor.write(BACKWARD, 0)
            print "Going from PICKUP to FIND"
            self.startFindModule()
            return

    ## Checks if all initialization processes went smoothly.
    def checkForInitializationErrors(self):
        assert not self.vision.isScreenBlack()

    ## Check what color a freshly caught block is.
    #
    # @return 0 if the color sensor does not see a block.
    #         1 if the color sensor sees a red block
    #         2 if the color sensor sees a green block
    def checkForBlock(self):
        # TODO
        raise NotImplementedError

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()