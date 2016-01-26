# follow.py

from module import Module
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class FollowModule(Module):
    
    def __init__(self, timer, stepTimer, leftMotor, rightMotor, wallFollow, forwardSpeed, blockSwitch):
        self.timer = timer
        self.stepTimer = stepTimer
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.movement = wallFollow
        self.forwardSpeed = forwardSpeed
        self.blockSwitch = blockSwitch


    def start(self):
        self.timer.reset()

    def run(self):
        
        # usually wall follow for 10 seconds
        if self.timer.millis() < 10000:
            if self.stepTimer.millis() > 100:
                self.stepTimer.reset()
                if self.blockSwitch.val:
                    print "Going from FOLLOW to CHECK"
                    return MODULE_CHECK
                self.movement.followWall(self.movement.distance(),-FORWARD_SPEED)

        # turn aggressively for .3 seconds in case of being stuck
        elif self.timer.millis() < 13000:
            self.left.write( 0, 145)
            self.right.write( 1, 145)
        
        # reset everything and start over
        else:
            self.timer.reset()
            self.left.write(0,0)
            self.right.write(0,0)

        return MODULE_FOLLOW