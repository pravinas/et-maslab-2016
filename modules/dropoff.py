## dropoff.py
#
# Implements the DROPOFF module of the competition code.

from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class DropoffModule(Module):
    def __init__(self, timer, servo, motorRight, motorLeft, encoder):
        self.timer = timer
        self.servo = servo
        self.encoder = encoder
        self.encval = 0 

        self.motorRight = motorRight
        self.motorRight.write(1,0)
        self.motorLeft = motorLeft
        self.motorLeft.write(1,0)

    ## Set up the beginning of the dropoff process.
    def start(self):
        # TODO: Make sure that the cube drop-off location is actually good
        self.timer.reset()
        self.encval = self.encoder.val
        self.servo.write(SERVO_OPEN)

    ## Open the back door and drive "forwards," avoiding what needs to be avoided.
    #
    # @return   The value of the next module to return to.
    def run(self):

        # Allow timeout.
        if self.timer.millis() > DROPOFF_TIMEOUT:
            print "Timed out from DROPOFF to FOLLOW"
            self.motorRight.write(0,0)
            self.motorLeft.write(0,0)
            self.servo.write(SERVO_CLOSE)
            return MODULE_FOLLOW

        if self.timer.millis() > DROPOFF_WAIT_TIME and self.encoder.val < self.encval + DROPOFF_ENC_MAX:
            self.motorRight.write(0,FORWARD_SPEED)
            self.motorLeft.write(0,FORWARD_SPEED)

        # After robot moves forward enough, stop moving and close the door
        if self.encoder.val > self.encval + DROPOFF_ENC_MAX:
            self.motorRight.write(0,0)
            self.motorLeft.write(0,0)
            self.servo.write(SERVO_CLOSE)


        return MODULE_DROPOFF
