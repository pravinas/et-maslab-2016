## find.py
#
# Implements the FIND module of the competition code.

from tamproxy import Timer
from tamproxy.devices import Motor, Color, Encoder
from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from control import GoStraight
from logic import Logic
from constants import *

class FindModule(Module):

    def __init__(self, timer, leftMotor, rightMotor, intakeMotor, vision, logic):

        # Timeout to make sure we don't run over.
        self.timeout = 20000

        # Module timer
        self.timer = timer

        # GoStraight object to control movement
        self.movement = GoStraight(leftMotor, rightMotor, Timer())

        self.intakeMotor = intakeMotor

        # Timer object describing how much time has passed since the last 
        # camera input was processed.
        self.cameraTimer = Timer()
        # Time in milliseconds between pictures being taken.
        self.cameraTimeout = 100
        # Vision object to read data from the camera.
        self.vision = vision

        self.blockTimer = Timer()

        # Logic object for calculations
        self.logic = logic

        self.target = None
    
    ## Set up the beginning of the find process.
    def start(self):
        self.target = None
        self.updateTime = 0
        self.movement.reset()
        self.timer.reset()
        self.intakeMotor.write(0, 120)

    ## Try to find and move towards blocks on the map.
    # 
    # Turn until color is detected.
    # Drive towards largest color until it is centered on the screen.
    #
    # @param arbitraryTarget    A target angle to tell the robot it wants to reach.
    # @return   The value of the next module to return to.
    def run(self, arbitraryTarget = 0):
        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from FIND to FOLLOW"
            self.intakeMotor.write(0, 0)
            return MODULE_PICKUP

        # Check if we need to exit the module.
        # TODO: Make this actually work
        if self.blockTimer.millis() > 100:
            self.blockTimer.reset()
            if self.logic.checkForBlock() > 0 : 
                print "Going from FIND to PICKUP"
                self.intakeMotor.write(0, 0)
                return MODULE_PICKUP

        ## Capture an image from the camera every so often
        if self.cameraTimer.millis() > self.cameraTimeout:
            self.cameraTimeout = 100
            self.cameraTimer.reset()

            self.target = self.logic.findTarget(*self.vision.processImage())
            print self.target
            self.updateTime = self.timer.millis()

        # just go straight for a while once alligned
        if self.target != None:
            if abs(self.target) < 5 and self.timer.millis() > 1000 and self.target != 0:
                self.target = 0
                self.cameraTimeout = 500

        # Check if we see anything of interest on the screen.
        if self.target == None:
            self.movement.move_to_target(arbitraryTarget)
            # TODO: Make sure not to enter this subroutine when there is a block in the blind spot.
        else:
            self.movement.move_to_target(self.target)
            self.logic.bayesianTargetUpdate(self.target)

        return MODULE_FIND


