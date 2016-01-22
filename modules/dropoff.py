## dropoff.py
#
# Implements the DROPOFF module of the competition code.

from module import Module

from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class DropoffModule(Module):
    def __init__(self, timer, servo, motorRight, motorLeft, doorTimer):
        self.timeout = 7000
        self.waitTime = 500     # Time in ms to wait for the door to actually open.
        self.openValue = 90     # Value in degrees the servo should be when the door is open.
        self.closedValue = 180  # Value in degrees the servo should be when the door is closed.
        self.timer = timer
        self.servo = servo

        self.motorRight = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        self.motorRight.write(1,0)
        self.motorLeft = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        self.motorLeft.write(1,0)

        self.doorTimer = doorTimer

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
            return MODULE_FIND

        # After Door opens, go forward
        if self.timer.millis() > self.waitTime:
            self.doorTimer.reset()
            self.motorRight.write(0,FORWARD_SPEED)
            self.motorLeft.write(0,FORWARD_SPEED)

            # After robot moves forward enough, stop moving and close the door
            if self.doorTimer.millis() > 3000:
                self.motorRight.write(0,0)
                self.motorLeft.write(0,0)
                self.servo.write(self.closedValue)
                return MODULE_DROPOFF
        
        return MODULE_DROPOFF
