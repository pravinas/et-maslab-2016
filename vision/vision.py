# vision.py
#
# A module for processing images from a webcam.

import cv2
import numpy as np

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

## Color functions: Take a numpy array as input, and return a boolean array.
GREEN = lambda img: np.logical_and(img.T[1] > 1.1 * img.T[0], img.T[1] > 1.1 * img.T[2]).T
RED   = lambda img: np.logical_and(img.T[2] > 1.3 * img.T[0], img.T[2] > 1.3 * img.T[1]).T

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

    ## Ariel's algorithm for color filtering.
    # 
    # @param img An image array in BGR format.
    # @param matcherFn A function that turns a numpy array into a numpy with the color highlighted.
    # @return An image array where the proper colors are highlighted.
    def filterBGR(self, img, matcherFn):
        binFilter = np.array([0,255], dtype=np.uint8)
        newImg = np.choose(matcherFn(img), binFilter)

        return newImg


    ## Clean up a binary image array using a morphological opening function.
    #
    # @param img A binary image array
    # @return A cleaned up version of the input image.
    def morph(self, img):
        kernel = np.ones((2,2), np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 3)

    ## Take an input binary image and find the largest block in it.
    #
    # @param img A cleaned up binary image.
    # @return A list of BlockImg objects.
    def findLargestBlock(self, img, stacksOnly=False):
        image, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        blocks = []

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if stacksOnly:
                if h > 2.3 * w:
                    blocks.append(BlockImg(x + 0.5 * w, y + h, h))
            else:
                blocks.append(BlockImg(x + 0.5 * w, y + h, h))

        return sorted(blocks, key = lambda x: x.height, reverse = True)[0]

    ## Subroutine of the Vision module, intended to run once every second or so.
    # 
    # @return   A tuple of two lists of BlockImg objects, from largest to smallest area.
    #           The first list contains the blocks of our color, and the second list contains stacks.
    def processImage(self):
        retval, frame = self.capture.read()

        blockImg = self.filterBGR(frame, RED if self.myColorIsRed else GREEN)
        otherImg = self.filterBGR(frame, GREEN if self.myColorIsRed else RED)
        stackImg = cv2.bitwise_or(otherImg, blockImg)

        blockImg = self.morph(blockImg)
        stackImg = self.morph(stackImg)

        if self.debug:
            cv2.imwrite("frame.png", frame)
            cv2.imwrite("blockimg.png", cv2.cvtColor(blockImg, cv2.COLOR_GRAY2BGR))
            cv2.imwrite("otherimg.png", cv2.cvtColor(otherImg, cv2.COLOR_GRAY2BGR))
            cv2.imwrite("stackimg.png", cv2.cvtColor(stackImg, cv2.COLOR_GRAY2BGR))

        block = self.findLargestBlock(blockImg)
        stack = self.findLargestBlock(stackImg)

        return (block, stack)

    ## Distinguish if the whole screen is black, for troubleshooting.
    #
    # @return Whether or not the whole screen is black.
    def isScreenBlack(self):
        retval, frame = self.capture.read()
        return not np.any(frame)


        