#Go_straight.py
import math
import tamproxy
from ..firmware.test_gyro import GyroRead



class TestControl(Sketch):
    def setup(self):
        # just used the code from test_motor for this part
        # assume motor 1 is left and motor 2 is right side
        # just connects to motors not sure what else to do here
        # todo
        self.motor1 = Motor(self.tamp, 3, 4)
        self.motor1.write(1,0)
        self.motor2 = Motor(self.tamp, 5, 6)
        self.motor2.write(1,0)
        self.delta = 1
        self.motorval = 0
        self.timer = Timer()

    # using the gyro to correct
    # will make bot go straight 
    # motor1 = left
    # motor2 = right  
    # todo

    def loop(self):

    	#this is motorval up to 255 
        base_speed = 100
        #need to make added speed a function of PID
        added_speed = 50


        # not sure how gyro values will apear
        # need to check

        if (self.timer.millis() > 10000):
        	self.timer.reset()
        # assumes spin up is + while spin down - 
        # this is the basic structure of what will happen
        # only takes into account gyro values
        # todo
        # going to work on PID


        if GyroRead < 0:
        	self.motor1.write(0,base_speed)
        	self.motor2.write(1,base_speed + added_speed)
        elif GyroRead > 0:
        	self.motor1.write(0,base_speed + added_speed)
        	self.motor2.write(1,base_speed)
        else:
        	self.motor1.write(0,base_speed)
        	self.motor2.write(1,base_speed)

        #PID base is here
        p = 1
        i = .9
        d = .1

        err = 0 - GyroRead

		kp = p*err
		Ki = integrate[i*err]
		kd = differentiate[d*err]
		power = kp + ki + kd
		self.motor1.write(0,base_speed + power)
		self.motor2.write(1,base_speed - power)

