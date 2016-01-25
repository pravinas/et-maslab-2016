#Wall_Follow.py
#when run returns no module long_range_ir

from tamproxy import Timer
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from control import GoStraight
from constants import *

class WallFollow():

    ## Initialize a WallFollowing.
    #
    # @param left   A Motor representing the left motor.
    # @param right  A Motor representing the right motor.
    # @param timer  A Timer for moderating data taking.
    def __init__(self, left, right, timer, ir0, ir1, ir2, ir3):
        self.leftMotor = left
        self.rightMotor = right
        self.timer = Timer()
        self.timer.reset()
        self.ir0 = ir0
        self.ir1 = ir1
        self.ir2 = ir2
        self.ir3 = ir3

        # Number of values to record
        self.recordLen = 10
        # Record of values from youngest to oldest.
        self.record = []

        # Tweak values as needed
        self.kp = 0.9
        self.ki = -0.00005
        self.kd = -0.2


    ## get distance value from ir sensors
    # returns distance from edge of bot to wall
    #
    # if statement determines which wall is nearest

    def distance(self):
        # TODO: This is hacky. Fix it to be nice, or at least well-docced.

        # comment below only uses front right IR
        # no corner problem
        # issue: drives right when approachin wall and can't follow it

        # uses both front IRs returns value of nearest one
        # calls corner if too close to wall with both IRs

        if self.ir1.read_ir() + self.ir0.read_ir() < 90:

            self.corner(self)

        if self.ir1.read_ir()  < self.ir0.read_ir():
            #right wall nearer 
            return (self.ir1.read_ir()) 
        else: 
            #left wall nearer
            return -(self.ir0.read_ir())

    ## Given a distance value from distance make bot move to be 14 cm from wall.
    #
    # @param distance a number proportional to the distance between the edge of robot and wall
    #                   
    # @param speed  A value from -255 to 255 that corresponds to the general 
    #               speed of the robot.

    def followWall(self, distance, speed):

        if self.timer.millis() > 100:
            self.timer.reset()


            # error value
            # 50 from hypotenuse of a 45,45,90
            err = 50 - distance

            # Integrate over the last several timesteps.
            self.record.insert(0, err)
            if len(self.record) > self.recordLen:
                self.record.pop()

            # Take the derivative over recorded history.
            deriv = self.record[0] - self.record[-1] if len(self.record) > 1 else 0

            power = self.kp * err + self.kd * deriv + self.ki * sum(self.record) 

            self.leftMotor.write ((speed - power) > 0, min(abs(speed - power), 255))
            self.rightMotor.write((speed + power) > 0, min(abs(speed + power), 255))

    ## Makes bot turn spinup(counter clockwise if too close to wall)
    # will stop once IR0 is significantly smaller in value than IR1
    # once reaching corner will follow wall on right, need to fix for left
    # todo
    def corner(self):
        #not sure how to write motors
        #todo

        self.leftMotor.write (1, 255)
        self.rightMotor.write(1, 255)
        
        if self.timer.millis() > 100:
            self.timer.reset()

            # once right IR is 30 cm less in value, bot will resume following wall.

            if (self.ir1.read_ir() + 30) < self.ir0.read_ir():
            
                self.followWall(self.distance(),-30)



    ## Reinitialize this class to start taking data over.
    def reset(self):
        self.timer.reset()
        self.record = []