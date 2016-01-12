#Go_straight.py

class Go_straight():

    ## Initialize a Go_straight object.
    #
    # @param left   A Motor representing the left motor.
    # @param right  A Motor representing the right motor.
    def __init__(self, left, right, gyro, timer):
        self.leftMotor = left
        self.rightMotor = right
        self.gyro = gyro
        self.timer = timer
        self.timer.reset()

    ## Given a target angle different from where we are currently facing,
    #  move to face that angle.
    #
    # @param theta  A number proportional to the angle off from which the
    #               robot is facing.
    def move_to_target(self, theta):
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

			self.leftMotor.write(0,base_speed - power)
			self.rightMotor.write(1,base_speed + power)

