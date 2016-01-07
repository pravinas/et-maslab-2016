# test_control.py
# 
# Run a sketch that tells the robot to run various control routines.

import tamproxy

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
		pass

	def loop(self):
		# motor1 = left
		# motor2 = right
		# using graphical representation Ariel gave us theta v time to think about problem
		# same timer as previous need to tweak
		# todo
		if (self.timer.millis() > 10):
            self.timer.reset()

            # θ > 0 means need to turn left
            # θ < 0 means need to turn right
            # θ = 0 means we happy :D
            # assumed always going forward so directions is always 1
            # changes need to be done to this below
            # need to include dampening and other stuff
            # magnitude must be a function of (θ, G(if have gyro), microcontrollers, and time) 
            #todo

            if θ > 0:
            # need to make motor2 faster for some value
            # todo
            	self.motor1.write(0, abs(self.motorval))
            	self.motor2.write(1, abs(self.motorval))
            elif θ < 0:
            # need to make motor 1 faster for some value
            #todo
            	self.motor1.write(0, abs(self.motorval))
            	self.motor2.write(1, abs(self.motorval))
            else:
            # need to decide on some magnitude 
            #todo
            	self.motor1.write(0, abs(self.motorval))
            	self.motor2.write(1, abs(self.motorval))

		pass