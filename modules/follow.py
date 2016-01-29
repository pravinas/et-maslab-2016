# follow.py

from module import Module
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class FollowModule(Module):
    
    def __init__(self, timer, leftMotor, rightMotor, intakeMotor, wallFollow, forwardSpeed, blockSwitch):
        self.timer = timer
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.intakeMotor = intakeMotor
        self.movement = wallFollow
        self.forwardSpeed = forwardSpeed
        self.blockSwitch = blockSwitch


    def start(self):
        self.timer.reset()
        #turn intake on
        self.intakeMotor.write(INTAKE_IN, INTAKE_POWER)

    def run(self):
        # usually wall follow for a few seconds
        if self.timer.millis() < FOLLOW_WALL_TIME:
            #print "follow blockswitch", bool(self.blockSwitch.val)
            if self.blockSwitch.val:
                print "Going from FOLLOW to CHECK"
                self.intakeMotor.write(0,0)
                self.leftMotor.write(0,0)
                self.rightMotor.write(0,0)
                return MODULE_CHECK
            self.movement.followWall(self.movement.distance(), FORWARD_SPEED)

        # Back up a little
        elif self.timer.millis() < FOLLOW_WALL_TIME + FOLLOW_BACK_TIME:
            self.leftMotor.write(BACKWARD_DIR, FOLLOW_BACKUP_SPEED)
            self.rightMotor.write(BACKWARD_DIR, FOLLOW_BACKUP_SPEED)

        # turn aggressively for .3 seconds in case of being stuck
        elif self.timer.millis() < FOLLOW_WALL_TIME + FOLLOW_BACK_TIME + FOLLOW_TURN_TIME:
            self.leftMotor.write(FORWARD_DIR, TURN_FAST_SPEED)
            self.rightMotor.write(BACKWARD_DIR, TURN_FAST_SPEED)
        
        # reset everything and start over
        else:
            self.timer.reset()
            self.leftMotor.write(0,0)
            self.rightMotor.write(0,0)

        return MODULE_FOLLOW
