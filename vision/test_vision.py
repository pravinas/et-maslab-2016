# test_vision.py
#
# Tests some functions in vision.py.

# TODO: Write the following code.
# __init__ only once, before running anything else.
# Check isScreenBlack() before continuing.
# processImage() continuously with a webcam.

from vision import Vision
import time

vision = Vision(False, debug=True)

if vision.isScreenBlack():
	print "The screen appears to be black."

for i in range(10):
	print "~~~~~~~~~"
	print i, vision.processImage()
	time.sleep(0.5)