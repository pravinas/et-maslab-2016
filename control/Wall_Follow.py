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
        self.kp = 0.5
        self.ki = 0.1
        self.kd = 0.4


    ## get distance value from ir sensors
    # returns distance from edge of bot to wall
    #
    # if statement determines which wall is nearest
    # returns distance of side of robot to wall

    def distance(self):
        # TODO: This is hacky. Fix it to be nice, or at least well-docced.
        if self.ir1.read_ir() + self.ir3.read_ir() < self.ir0.read_ir() + self.ir2.read_ir():
            return (self.ir1.read_ir() + self.ir3.read_ir())/2
        else:
            return -((self.ir0.read_ir() + self.ir2.read_ir())/2)

    ## Given a distance value from distance make bot move to be 14 cm from wall.
    #
    # @param distance a number proportional to the distance between the edge of robot and wall
    #                   
    # @param speed  A value from -255 to 255 that corresponds to the general 
    #               speed of the robot.

    def followWall(self, distance, speed):

        if self.timer.millis() > 1000:
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

            power = self.kp * err + self.ki * sum(self.record) + self.kd * deriv

            self.leftMotor.write ((speed + power) > 0, min(abs(speed + power), 255))
            self.rightMotor.write((speed - power) > 0, min(abs(speed - power), 255))


    ## Reinitialize this class to start taking data over.
    def reset(self):
        self.timer.reset()
        self.record = []