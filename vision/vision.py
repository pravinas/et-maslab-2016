# vision.py
#
# A module for processing images from a webcam.

import cv2
import numpy as np

## Define a color as a limit between min and max HSV.
class Color():
    def __init__(self, h_min, h_max, s_min, s_max, v_min, v_max):
        self.h_min = h_min
        self.h_max = h_max
        self.s_min = s_min
        self.s_max = s_max
        self.v_min = v_min
        self.v_max = v_max

## Define an image of a block as a location on a screen and its area.
# (0, 0) is the upper left hand corner of the screen.
#
# @param x The x coordinate of the block's center. Increases to the right.
# @param y The y coordinate of the block's southern extreme. Increases downwards.
# @param h The height of the block in pixels.
class BlockImg():
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

BLACK = Color(0, 255, 20, 255, 0, 20)       ## The color Black
WHITE = Color(0, 255, 0, 25, 240, 255)      ## The color White
BLUE  = Color(100, 140, 100, 200, 50, 255)  ## The color Blue
GREEN = Color(37, 96, 50, 255, 40 255)      ## The color Green
RED   = Color(150, 15, 50, 255, 50, 255)     ## The color Red

class Vision():

    ## Create an instance of the Vision module.
    #
    # @param myColorIsRed True if we are collecting red 
    def __init__(self, myColorIsRed):
        self.myColor = RED if myColorIsRed else GREEN
        self.unColor = GREEN if myColorIsRed else RED
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CV_CAP_PROP_FRAME_WIDTH, 160); # X resolution
        self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 120); # Y resolution

    ## Turn a color image into a binary image where colors within the tolerance
    # are highlighted.
    #
    # @param img An image array.
    # @param color The Color to filter.
    # @return An image array where the proper colors are highlighted.
    def filterHSV(self, img, color):
        if (color.h_min > color.h_max):
            out1 = cv2.inRange(img, np.array([color.h_max, color.s_min, color.v_min]), np.array([179, color.s_max, color.v_max]))
            out2 = cv2.inRange(img, np.array([0, color.s_min, color.v_min]), np.array([color.h_min, color.s_max, color.v_max]))
            return cv2.bitwise_or(out1, out2)
        else:
            return cv2.inRange(img, np.array([color.h_min, color.s_min, color.v_min]), np.array([color.h_max, color.s_max, color.v_max]))

    ## Clean up a binary image array using a morphological opening function.
    #
    # @param img A binary image array
    # @return A cleaned up version of the input image.
    def morph(self, img):
        kernel = np.ones((5,5), np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    ## Take an input binary image and find the blocks in it.
    #
    # @param img A cleaned up binary image.
    # @return A list of BlockImg objects.
    def findBlocksInBinaryImage(self, img, stacksOnly=False):
        image, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        blocks = []

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if stacksOnly:
                if h > 2.5 * w:
                    blocks.append(Block(x + 0.5 * w, y + h, h))
            else:
                blocks.append(Block(x + 0.5 * w, y + h, h))

        return blocks

    ## Subroutine of the Vision module, intended to run once every second or so.
    # 
    # @return   A tuple of two lists of BlockImg objects, from largest to smallest area.
    #           The first list contains the blocks of our color, and the second list contains stacks.
    def processImage(self):
        retval, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        blockImg    = self.filterHSV(frame, self.myColor)
        stackImg    = cv2.bitwise_or(ourImg, self.filterHSV(frame, self.unColor))

        blockImg    = self.morph(ourImg)
        stackImg    = self.morph(stackImg)

        blocks  = sorted(self.findBlocksInBinaryImage(blockImg, False), key = lambda x: x.area, reverse = True)
        stacks  = sorted(self.findBlocksInBinaryImage(stackImg, True), key = lambda x: x.area, reverse = True)

        return (blocks, stacks)

    ## Distinguish if the whole screen is black, for troubleshooting.
    #
    # @return Whether or not the whole screen is black.
    def isScreenBlack(self):
        retval, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blackImg = self.filterHSV(frame, BLACK)
        blackImg = self.morph(blackImg)

        return len(cv2.findContours(blackImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[2]) < 2


        