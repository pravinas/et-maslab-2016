# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer
from vision import Vision
from pubsub import Publisher

# List of Modules/States
# TODO Document the constants here
MODULE_FIND     = {num: 0, timeout: 7000, blocks: [], stacks: []}
MODULE_PICKUP   = {num: 1, timeout: 7000}
MODULE_DROPOFF  = {num: 2, timeout: 7000}

RED = True
GREEN = not RED

class Robot(SyncedSketch):

    def setup(self):
        self.module = MODULE_FIND
        self.moduleTimer = Timer()

        self.blockColor = RED

        self.vision = Vision(self.blockColor)
        self.visionPublisher = Publisher()
        self.cameraTimer = Timer()
        self.cameraTimeout = 500 # Calibrate if the robot ultimately acts weird for no reason.

        self.checkForInitializationErrors()

    def loop(self):
        self.checkTimeouts()

        if (self.module[num] == MODULE_FIND[num]):
            self.runFindModule()

        elif (self.module[num] == MODULE_PICKUP[num]):
            self.runPickupModule()

        elif (self.module[num] == MODULE_DROPOFF[num]):
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
        assert MODULE_FIND = self.module

        ## Capture an image from the camera every so often
        if self.cameraTimer.millis() > self.cameraTimeout:
            self.cameraTimer.reset()
            self.module[blocks], self.module[stacks] = self.vision.processImage()

        # TODO: Make this flexible whether or not we are using red or green blocks.
        if len(blocks) + len(stacks) == 0:
            # TODO (High priority): Turn to look for blocks.
            # TODO (Low priority): Make sure not to enter this subroutine when there is a block in the blind spot.
        else:
            target = blocks[0]
            # TODO: Drive towards the target.

    def runPickupModule(self):
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

    ## Change the active module if the timeout is reached.
    def checkTimeouts(self):
        # TODO
        raise NotImplementedError

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()