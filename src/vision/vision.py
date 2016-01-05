import cv2
import numpy as np

class Color():
    def __init__(self, h_min, h_max, s_min, s_max, v_min, v_max):
        self.h_min = h_min
        self.h_max = h_max
        self.s_min = s_min
        self.s_max = s_max
        self.v_min = v_min
        self.v_max = v_max

class BlockImg():
    def __init__(self, x, y, area):
        self.x = x
        self.y = y
        self.area = area

BLACK = Color(0, 255, 20, 255, 0, 20)
WHITE = Color(0, 255, 0, 25, 240, 255)
BLUE  = Color(100, 140, 100, 200, 50, 255)
GREEN = Color(37, 96, 50, 255, 40 255)
RED  = Color(150, 15, 50, 255, 50, 255)

class Vision():
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CV_CAP_PROP_FRAME_WIDTH, 320); # X resolution
        self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 240); # Y resolution

    def filterHSV(self, img, color):
        if (color.h_min > color.h_max):
            out1 = cv2.inRange(img, np.array([color.h_max, color.s_min, color.v_min]), np.array([179, color.s_max, color.v_max]))
            out2 = cv2.inRange(img, np.array([0, color.s_min, color.v_min]), np.array([color.h_min, color.s_max, color.v_max]))
            return cv2.bitwise_or(out1, out2)
        else:
            return cv2.inRange(img, np.array([color.h_min, color.s_min, color.v_min]), np.array([color.h_max, color.s_max, color.v_max]))

    def morph(self, img):
        kernel = np.ones((5,5), np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    def findBlocksInBinaryImage(self, img):
        image, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        blocks = []

        for contour in contours:
            moment = c2.moments(contour)
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            area = cv2.contourArea(cnt)
            blocks.append(Block(x, y, area))

    def loop(self):
        retval, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        greenImg = self.filterHSV(frame, GREEN)
        redImg   = self.filterHSV(frame, RED)

        greenImg = self.morph(greenImg)
        redImg   = self.morph(redImg)

        greenBlocks = self.findBlocksInBinaryImage(greenImg)
        redBlocks   = self.findBlocksInBinaryImage(redImg)

        return (greenBlocks, redBlocks)

    def isScreenBlack(self):
        retval, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blackImg = self.filterHSV(frame, BLACK)
        blackImg = self.morph(blackImg)

        return len(cv2.findContours(blackImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[2]) < 2


        