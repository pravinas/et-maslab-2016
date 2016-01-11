# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor
from vision import Vision
from pubsub import Publisher

# List of Modules/States
# TODO Document the constants here
MODULE_FIND     = {"name": "FIND"   , "timeout": 7000, "blocks": [], "stacks": []}
MODULE_PICKUP   = {"name": "PICKUP" , "timeout": 7000}
MODULE_DROPOFF  = {"name": "DROPOFF", "timeout": 7000}

RED = True
GREEN = not RED
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

        # Motor object representing the left motor.
        self.leftMotor = Motor(self.tamp, 1, 2)
        # Motor object representing the right motor.
        self.rightMotor = Motor(self.tamp, 3, 4)
        # TODO: Figure out which pins are hooked up where.

        self.checkForInitializationErrors()

    def loop(self):
        self.checkTimeouts()

        if (self.module["num"] == MODULE_FIND["num"]):
            self.runFindModule()

        elif (self.module["num"] == MODULE_PICKUP["num"]):
            self.runPickupModule()

        elif (self.module["num"] == MODULE_DROPOFF["num"]):
            # TODO
            pass

        else:
            print "Unexpected module number:", self.module
            raise Exception()

    ## Try to find and move towards blocks on the map.
    # 
    # Turn until color is detected.
    # Drive towards largest color until it is centered on the screen.
    def runFindModule(self):
        assert MODULE_FIND == self.module

        # Check if we need to exit the module.
        if self.checkForBlock() > 0 or self.moduleTimer.millis() > self.module["timeout"]:
            self.module = MODULE_PICKUP
            self.moduleTimer.reset()

        ## Capture an image from the camera every so often
        if self.cameraTimer.millis() > self.cameraTimeout:
            self.cameraTimer.reset()
            self.module["blocks"], self.module["stacks"] = self.vision.processImage()

        blocks = self.module["blocks"]
        stacks = self.module["stacks"]

        # Check if we see anything of interest on the screen.
        if len(blocks) + len(stacks) == 0:
            # TODO (High priority): Turn to look for blocks.
            # TODO (Low priority): Make sure not to enter this subroutine when there is a block in the blind spot.
        else:
            target = blocks[0]
            if len(blocks) == 0:
                target = stacks[0]
            # TODO: Drive towards the target.


    def runPickupModule(self):
        assert MODULE_PICKUP == self.module
        # TODO
        raise NotImplementedError

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

    ## Change the active module if the "timeout" is reached.
    def checkTimeouts(self):
        # TODO
        raise NotImplementedError

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()