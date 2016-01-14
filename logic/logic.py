## logic.py
#
# File for algorithms that turn sensor data into more useful information.
from math import atan

class Logic():
    def __init__(self, imgWidth, imgHeight):
        self.imgWidth = imgWidth
        self.imgHeight = imgHeight
        
    ## Given the camera data, outputs an angle at which the robot should move.
    #
    # @param block  The block data that is output from the camera.
    # @param stack  The stack data that is output from the camera.
    # @return   An angle in rads corresponding to the block, if it exists, otherwise an 
    #           angle corresponding to the stack. If neither exists, return None.
    def findTargetFromCameraData(self, block, stack):
        if block.height == 0:
            if stack.height == 0:
                return None
            else:
                targetImg = stack
        else:
            targetImg = block

        x = (self.imgWidth/2 - targetImg.x) * targetImg.y
        y = self.imgHeight - targetImg.y


        # TODO: This needs to be calibrated from its position on the robot itself. 
        #       Should be a constant factor.
        k = 1.0

        return atan(k * x / y)

    ## Given the current target angle, use sensor data to update.
    #
    # @param target The current target angle.
    # @param time   The number of milliseconds that have passed since last update.
    def bayesianTargetUpdate(self, target):
        # TODO: Definitely need more arguments. Need to think about how to implement.
        return target