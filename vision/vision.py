# vision.py
#
# A module for processing images from a webcam.

import cv2
import numpy as np
import numpy.lib.index_tricks as ndi

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
        self.height = h

    def __repr__(self):
        return "Block: " + str((self.x,self.y,self.height))

BLACK = Color(0, 255, 20, 255, 0, 20)       ## The color Black
WHITE = Color(0, 255, 0, 25, 240, 255)      ## The color White
BLUE  = Color(100, 140, 100, 200, 50, 255)  ## The color Blue
GREEN = Color(37, 96, 50, 230, 40, 230)     ## The color Green
RED   = Color(150, 15, 50, 230, 50, 230)    ## The color Red

class Vision():

    ## Create an instance of the Vision module.
    #
    # @param myColorIsRed True if we are collecting red 
    def __init__(self, myColorIsRed, debug=False):
        self.myColorIsRed = myColorIsRed
        self.capture = cv2.VideoCapture(1)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 80); # X resolution
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 60); # Y resolution
        self.debug = debug

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

    ## Ariel's algorithm for color filtering.
    # 
    # @param img An image array in BGR format.
    # @param matcherFn Are we filtering red or not?
    # @return An image array where the proper colors are highlighted.
    def filterBGR(self, img, isRed):
        binFilter = np.array([0,255], dtype=np.uint8)

        if isRed:
            newImg = np.choose(np.logical_and(img.T[2] > 1.3 * img.T[0], img.T[2] > 1.3 * img.T[1]).T, binFilter)
        else: 
            newImg = np.choose(np.logical_and(img.T[1] > 1.3 * img.T[0], img.T[1] > 1.3 * img.T[2]).T, binFilter)

        return newImg


    ## Clean up a binary image array using a morphological opening function.
    #
    # @param img A binary image array
    # @return A cleaned up version of the input image.
    def morph(self, img):
        kernel = np.ones((2,2), np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 3)

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
                if h > 2.3 * w:
                    blocks.append(BlockImg(x + 0.5 * w, y + h, h))
            else:
                blocks.append(BlockImg(x + 0.5 * w, y + h, h))

        return blocks

    ## Subroutine of the Vision module, intended to run once every second or so.
    # 
    # @return   A tuple of two lists of BlockImg objects, from largest to smallest area.
    #           The first list contains the blocks of our color, and the second list contains stacks.
    def processImage(self):
        retval, frame = self.capture.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #blockImg = self.filterHSV(frame, RED if self.myColorIsRed else GREEN)
        #otherImg = self.filterHSV(frame, GREEN if self.myColorIsred else RED)

        blockImg = self.filterBGR(frame, self.myColorIsRed)
        otherImg = self.filterBGR(frame, not self.myColorIsRed)

        stackImg = cv2.bitwise_or(otherImg, blockImg)

        blockImg = self.morph(blockImg)
        stackImg = self.morph(stackImg)

        if self.debug:
            #cv2.imwrite("frame.png", cv2.cvtColor(frame, cv2.COLOR_HSV2BGR))
            cv2.imwrite("frame.png", frame)
            cv2.imwrite("blockimg.png", cv2.cvtColor(blockImg, cv2.COLOR_GRAY2BGR))
            cv2.imwrite("otherimg.png", cv2.cvtColor(otherImg, cv2.COLOR_GRAY2BGR))
            cv2.imwrite("stackimg.png", cv2.cvtColor(stackImg, cv2.COLOR_GRAY2BGR))

        blocks = sorted(self.findBlocksInBinaryImage(blockImg, False), key = lambda x: x.height, reverse = True)
        stacks = sorted(self.findBlocksInBinaryImage(stackImg, True), key = lambda x: x.height, reverse = True)

        return (blocks, stacks)

    ## Distinguish if the whole screen is black, for troubleshooting.
    #
    # @return Whether or not the whole screen is black.
    def isScreenBlack(self):
        retval, frame = self.capture.read()
        #TODO
        return False


        