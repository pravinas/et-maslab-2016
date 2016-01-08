# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer
from vision import Vision
from pubsub import Publisher

# List of Modules/States
# 
# Properties:
#   - num: An ID number for this module.
#   - timeout: The maximum amount of time to spend on this module.
#              TODO: Calibrate timeouts.
#   - timer: The amount of time spent in this module so far.
MODULE_FIND     = {num: 0, timeout: 7000, timer: 0}
MODULE_PICKUP   = {num: 1, timeout: 7000, timer: 0}
MODULE_DROPOFF  = {num: 2, timeout: 7000, timer: 0}

RED = True
GREEN = not RED

class Robot(SyncedSketch):

    def setup(self):
        self.setModule(MODULE_FIND)
        self.moduleTimer = Timer()

        self.blockColor = RED

        self.vision = Vision(RED)
        self.visionPublisher = Publisher()
        self.cameraTimer = Timer()
        self.cameraTimeout = 500 # Calibrate if the robot ultimately acts weird for no reason.

        self.checkForInitializationErrors()

    def loop(self):
        self.checkTimeouts()

        if (self.module[num] == MODULE_FIND[num]):
            self.runFindModule()

        elif (self.module[num] == MODULE_PICKUP[num]):
            # TODO
            pass

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
        blocks = []
        stacks = []

        ## Capture an image from the camera every so often
        if self.cameraTimer.millis() > self.cameraTimeout:
            self.cameraTimer.reset()
            blocks, stacks = self.vision.processImage()

        # TODO: Make this flexible whether or not we are using red or green blocks.
        if len(blocks):
            # TODO (High priority): Turn to look for blocks.
            # TODO (Low priority): Make sure not to enter this subroutine when there is a block in the blind spot.
        else:
            target = redblocks[0]
            # TODO: Drive towards the target.


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

    ## Change the active module to another one.
    def setModule(self, module):
        self.module = module
        self.module[timer] = 0

    ## Change the active module if the timeout is reached.
    def checkTimeouts(self):
        # TODO
        raise NotImplementedError

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()