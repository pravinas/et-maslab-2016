#Wall_Follow.py

class WallFollow(self):
	## Initialize Wall Following
	#
    # @param left   A Motor representing the left motor.
    # @param right  A Motor representing the right motor.
    # @param timer  A Timer for moderating data taking.
	def __init__(self,left,right,timer):
		self.leftmotor = left
		self.rightmotor = right
		self.timer = timer
		self.timer.reset()

		# Number of values to record
        self.recordLen = 10
        # Record of values from youngest to oldest.
        self.record = []

        # Tweak values as needed
        self.kp = 1.0
        self.ki = 0.1
        self.kd = 0.5

		
	# Make module to give theta from LRIR inputs
	# TODO

	## Given value from LRIR sensors, makes bot move forward 
    #
    # @param theta A number proportional to the angle between the wall and 
    # 				where the bot is facing
    # @param speed  A value from -255 to 255 that corresponds to the general 
    #               speed of the robot.
	def Follow_Wall(self, theta, speed = 0):
		if self.timer.millis() > 100:
			self.timer.reset(0)

			# error value
            err = 0 - theta

            # Integrate over the last several timesteps.
            self.record.insert(0, err)
            if len(self.record) > self.recordLen:
                self.record.pop()

            # Take the derivative over recorded history.
            deriv = self.record[0] - self.record[-1] if len(self.record) > 1 else 0

            power = self.kp * err + self.ki * sum(self.record) + kd * deriv

            self.leftMotor.write ((speed - power) > 0, min(abs(speed - power), 255))
            self.rightMotor.write((speed + power) > 0, min(abs(speed + power), 255))


    ## Reinitialize this class to start taking data over.
    def reset(self):
        self.timer.reset()
        self.record = []


