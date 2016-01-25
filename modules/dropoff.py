## dropoff.py
#
# Implements the DROPOFF module of the competition code.

from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class DropoffModule(Module):
    def __init__(self, timer, servo, motorRight, motorLeft):
        self.timeout = 7000
        self.waitTime = 500     # Time in ms to wait for the door to actually open.
        self.waitTime2 = 1000   #Time in ms to wait for the robot to move forward and door to close.
        self.openValue = 100     # Value in degrees the servo should be when the door is open.
        self.closedValue = 172  # Value in degrees the servo should be when the door is closed.
        self.timer = timer
        self.servo = servo

        self.motorRight = motorRight
        self.motorRight.write(1,0)
        self.motorLeft = motorLeft
        self.motorLeft.write(1,0)

    ## Return True if there was an error in initialization, False otherwise.
    def checkForInitializationErrors(self):
        # soft TODO: Make sure servo is initialized in the "closed" position.
        return False

    ## Set up the beginning of the dropoff process.
    def start(self):
        # TODO: Make sure that the cube drop-off location is actually good
        self.timer.reset()
        self.servo.write(self.openValue)

    ## Open the back door and drive "forwards," avoiding what needs to be avoided.
    #
    # @return   The value of the next module to return to.
    def run(self):

        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from DROPOFF to FIND"
            self.motorRight.write(0,0)
            self.motorLeft.write(0,0)
            return MODULE_FIND

        # After Door opens, go forward
        if self.timer.millis() > self.waitTime and self.timer.millis() < self.waitTime2:
            self.motorRight.write(0,FORWARD_SPEED)
            self.motorLeft.write(0,FORWARD_SPEED)

        # After robot moves forward enough, stop moving and close the door
        if self.timer.millis() > self.waitTime2:
            self.motorRight.write(0,0)
            self.motorLeft.write(0,0)
            self.servo.write(self.closedValue)
        #After robot finishes closing the door, go to the next module
        if self.timer.millis() > self.waitTime + self.waitTime2:
            return MODULE_FIND

        return MODULE_DROPOFF
