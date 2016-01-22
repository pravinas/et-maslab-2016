## use this file to find the angle between the robot and the block

from logic import Logic
from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vision import Vision

logic = Logic()
vision = Vision(False, 80, 60, debug=True) #False = green, True = red

if vision.isScreenBlack():
	print "The screen appears to be black."

processed = vision.processImage()

block = processed[0]
stack = processed[1]

print logic.findTarget(block, stack)