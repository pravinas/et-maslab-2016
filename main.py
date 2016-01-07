# main.py
#
# The main sketch for the robot's processes.

from tamproxy import SyncedSketch, Timer

MODULE_FIND     = {num: 0, timeout: 7000}
MODULE_PICKUP   = {num: 1, timeout: 7000}
MODULE_DROPOFF  = {num: 2, timeout: 7000}

class Robot(SyncedSketch):

    def setup(self):
        self.setModule(MODULE_FIND)
        self.timer = Timer()

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
    #       Check screen 3x second.
    def runFindModule(self):
        # TODO
        pass

    ## Check what color a freshly caught block is.
    #
    # @return 0 if the color sensor does not see a block.
    #         1 if the color sensor sees a red block
    #         2 if the color sensor sees a green block
    def checkForBlock(self):
        # TODO
        pass

    ## Change the active module to another one.
    def setModule(self, module):
        self.module = module
        self.module[timer] = 0

    ## Change the active module if the timeout is reached.
    def checkTimeouts(self):
        # TODO
        pass

# main code:
if __name__ == "__main__":
    sketch = Robot(1, -0.00001, 100)
    sketch.run()