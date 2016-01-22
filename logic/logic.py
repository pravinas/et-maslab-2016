## logic.py
#
# File for algorithms that turn sensor data into more useful information.
from math import atan
from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class Logic():
    def __init__(self, color=None, leftEnc=None, rightEnc=None):
        self.imgWidth = CAMERA_WIDTH
        self.imgHeight = CAMERA_HEIGHT
        self.color = color
        self.leftEnc = leftEnc
        self.rightEnc = rightEnc
        
    ## Given the camera data, outputs an angle at which the robot should move.
    #
    # @param block  The block data that is output from the camera.
    # @param stack  The stack data that is output from the camera.
    # @return   An angle in rads corresponding to the block, if it exists, otherwise an 
    #           angle corresponding to the stack. If neither exists, return None.
    def findTarget(self, block, stack):
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
    def bayesianTargetUpdate(self, target):
        out = (self.rightEnc.val - self.leftEnc.val) / WHEEL_WIDTH
        self.rightEnc.write(0)
        self.leftEnc.write(0)
        return target + out

    
    ## Check what color a freshly caught block is.
    #
    # @return 0 if no block is caught
    #         1 if the color sensor sees our color of block.
    #         2 if the color sensor sees not our color of block.
    def checkForBlock(self):
        # TODO: Use limit switch to detect if block is caught.
        if r > 1.5*g and r > 1.5*b:
            return "Red"
        elif g > r and g > 1.2*b:
            return "Green"
        else:
            return "No Block"