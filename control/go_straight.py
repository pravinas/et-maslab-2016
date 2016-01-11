#Go_straight.py
import tamproxy
from ..firmware.test_gyro import GyroRead



class Go_straight(Sketch):
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

    def loop(self):
    	ki = 0
    	kd = 0
    	#this can be increased up to 255 
        base_speed = 100
		
        # PID base is here
        # very simple PID controller
        # need to adjust to get propper values
       	p = 1
       	i = .1
        d = .5

        if (self.timer.millis() < 2000):

	        # need to change to gyro value
	        # concerned about value of err during movement
    	    err = 0 - self.gyro.val

	        # proportional
			kp = p*err
			# integral/adding data points
			ki = [i*err] + ki
			# derivative new d*err - previous kd 
			kd = [d*err] - kd
			power = kp + ki + kd

			self.motor1.write(0,base_speed - power)
			self.motor2.write(1,base_speed + power)

