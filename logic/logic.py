## logic.py
#
# File for algorithms that turn sensor data into more useful information.
from math import atan
from tamproxy import Timer
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class Logic():
    def __init__(self, color, leftEnc, rightEnc):
        self.imgWidth = CAMERA_WIDTH
        self.imgHeight = CAMERA_HEIGHT
        self.color = color
        self.leftEnc = leftEnc
        self.rightEnc = rightEnc
        self.lastTarget = 0
        self.timer = Timer()


        
    ## Given the camera data, outputs an angle at which the robot should move.
    #
    # @param block  The block data that is output from the camera.
    # @param stack  The stack data that is output from the camera.
    # @return   An angle in rads corresponding to the block, if it exists, otherwise an 
    #           angle corresponding to the stack. If neither exists, return None.
    def findTarget(self, block, stack):
        if block.height == 0:
            if stack.height == 0:
                return self.lastTarget
            else:
                targetImg = stack
        else:
            targetImg = block
        # Turns out we don't care about the y value. Probably.
        # y = self.imgHeight - targetImg.y
        x = (self.imgWidth/2 - targetImg.x)
        

        # This converts pixels to radians
        k = .0093
        print "x = ", x
        self.lastTarget = atan(k*x)*180/3.14
        return self.lastTarget

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
    def checkForBlock(self, r, g, b):
        # TODO: Use limit switch to detect if block is caught. If we're going with a limit switch.
        if r > 1.6 * g and r > 1.6 * b:
            return 1 if RED else 2
        elif g > r and g > 1.2 * b:
            return 1 if GREEN else 2
        else:
            return 0