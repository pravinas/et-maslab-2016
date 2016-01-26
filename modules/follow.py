# follow.py

from module import Module
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from control.Wall_Follow import WallFollow
from logic import Logic
from constants import *

class FollowModule(Module):
    
    def __init__(self, timer, leftMotor, rightMotor, irBL, irBR, irFL, irFR, logic, forwardSpeed):
        self.timer = timer
        self.lastTime = 0
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.irBL = irBL
        self.irBR = irBR
        self.irFL = irFL
        self.irFR = irFR
        self.movement = WallFollow(self.leftMotor, self.rightMotor, self.timer, self.irFL, self.irFR, self.irBL, self.irBR)
        self.forwardSpeed = forwardSpeed
        self.logic = logic
        self.timeout = 5000

    def start(self):
        self.timer.reset()
        self.lastTime = 0

    def run(self):
        if self.timer.millis() > self.timeout:
            print "Timed out. Going to MODULE_FIND"
            return MODULE_FIND

        if self.timer.millis() - self.lastTime > 100:
            self.lastTime = self.timer.millis()
            self.movement.followWall(self.movement.distance(),self.forwardSpeed)
            #self.target = self.logic.findTarget(*self.vision.processImage())
            #if self.target != None:
            #    self.leftMotor.write(0,0)
            #    self.rightMotor.write(0,0)
            #    print "I found a block! I'll go there now in MODULE_FIND"
            #    return MODULE_FIND

        return MODULE_FOLLOW