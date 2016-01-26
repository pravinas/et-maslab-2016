# Check Module
# Checks to see what color the aquired block is, then spits out the block if it is the wrong color

from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class CheckModule(Module):

    def __init__ (self, timer, timeoutTimer, leftMotor, rightMotor, intakeMotor, color):
        self.timer = timer
        self.timeoutTimer = timeoutTimer
        self.timeout = 5000
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.intakeMotor = intakeMotor
        self.color = color
        self.needToCheckColor = True
        self.wrongBlock = False

    def start(self):
        self.timeoutTimer.reset()

    def run(self):
        # Timeout in case of issues
        if self.timeoutTimer.millis() > self.timeout:
            print "Timed out of CHECK going to FOLLOW"
            return MODULE_FOLLOW

        # Check what color the block is
        if self.needToCheckColor:
            if RED and self.color.r>1.6*self.color.g and self.color.r>1.6*self.color.b:
                print "Going from CHECK to PICKUP"
                return PICKUP_MODULE
            elif RED and self.color.g>self.color.r and self.color.g>1.2*self.color.b:
                self.wrongBlock = True
                self.needToCheckColor = False
                self.timer.reset()
            elif GREEN and self.color.g>self.color.r and self.color.g>1.2*self.color.b:
                print "Going from CHECK to PICKUP"
                return PICKUP_MODULE
            elif GREEN and self.color.r>1.6*self.color.g and self.color.r>1.6*self.color.b:
                self.wrongBlock = True
                self.needToCheckColor = False
                self.timer.reset()

        # spit out the block
        if self.wrongBlock:            
            if self.timer.millis() < 300
                # back up and spit out block
                self.intakeMotor.write(INTAKE_OUT,INTAKE_POWER)
                self.leftMotor.write(BACKWARD_DIR, FORWARD_SPEED)
                self.rightMotor.write(BACKWARD_DIR, FORWARD_SPEED)
            elif self.timer.millis() < 500:
                # turn left to avoid getting back the same block
                self.leftMotor.write(BACKWARD_DIR, TURN_FAST_SPEED)
                self.rightMotor.write(FORWARD_DIR, TURN_FAST_SPEED)
            else:
                # Stop and go back to following
                self.intakeMotor.write(0,0)
                self.leftMotor.write(0,0)
                self.rightMotor.write(0,0)
                print "Going from CHECK to FOLLOW"
                return MODULE_FOLLOW

        return MODULE_CHECK








