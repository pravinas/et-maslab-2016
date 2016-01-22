from tamproxy import Timer, SyncedSketch
from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from control import GoStraight
from logic import Logic
from constants import *


class TestFind(SyncedSketch):

    def setup(self):
        # Timeout to make sure we don't run over.
        self.timeout = 7000

        # Module timer
        self.timer = Timer()

        self.leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        self.rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        # GoStraight object to control movement
        self.movement = GoStraight(self.leftMotor, self.rightMotor, Timer())

        # Timer object describing how much time has passed since the last 
        # camera input was processed.
        self.cameraTimer = Timer()
        # Time in milliseconds between pictures being taken.
        self.cameraTimeout = 500
        # Vision object to read data from the camera.
        self.vision = Vision()

        # Logic object for calculations
        self.logic = Logic(True, 80, 60, debug=False) #False = green, True = red

        self.startThing()

    def loop(self):
        self.runThing()

    def startThing(self):
        self.target = None
        self.updateTime = 0
        self.movement.reset()
        self.timer.reset()

    def runThing(self):   
        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from FIND to FOLLOW"
            return MODULE_FOLLOW

        # Check if we need to exit the module.
        if self.logic.checkForBlock() > 0 : 
            print "Going from FIND to PICKUP"
            return MODULE_PICKUP

        ## Capture an image from the camera every so often
        if self.cameraTimer.millis() > self.cameraTimeout:
            self.cameraTimer.reset()

            self.target = self.logic.findTarget(*self.vision.processImage())
            self.updateTime = self.timer.millis()

        # Check if we see anything of interest on the screen.
        if target == None:
            self.movement.move_to_target(arbitraryTarget)
            # TODO: Make sure not to enter this subroutine when there is a block in the blind spot.
        else:
            self.movement.move_to_target(target)
            self.logic.bayesianTargetUpdate(target, self.timer.millis() - self.updateTime)


if __name__ == "__main__":
    sketch = TestFind(1, -0.00001, 100)
    sketch.run()