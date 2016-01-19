## find.py
#
# Implements the FIND module of the competition code.

from tamproxy import Timer
from control import GoStraight
from constants import *

class FindModule():

    def __init__(self, timer, leftMotor, rightMotor, vision, logic):

        # Timeout to make sure we don't run over.
        self.timeout = 7000

        # Module timer
        self.timer = timer

        # GoStraight object to control movement
        self.movement = GoStraight(leftMotor, rightMotor, Timer())

        # Timer object describing how much time has passed since the last 
        # camera input was processed.
        self.cameraTimer = Timer()
        # Time in milliseconds between pictures being taken.
        self.cameraTimeout = 500
        # Vision object to read data from the camera.
        self.vision = vision

        # Logic object for calculations
        self.logic = logic

        # Logic processor for sensor inputs.
        self.logic = Logic(self.vision.width, self.vision.height)

    
    ## Set up the beginning of the find process.
    def start(self):
        self.target = None
        self.updateTime = 0
        self.timer.reset()

    ## Try to find and move towards blocks on the map.
    # 
    # Turn until color is detected.
    # Drive towards largest color until it is centered on the screen.
    #
    # @param arbitraryTarget    A target angle to tell the robot it wants to reach.
    # @return   The value of the next module to return to.
    def run(self, arbitraryTarget = 60):
        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from FIND to PICKUP"
            return MODULE_PICKUP

        # Check if we need to exit the module.
        if self.checkForBlock() > 0 : 
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

        return MODULE_FIND
