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

		
	#IR input
	## Given value from LRIR sensor, makes bot move forward 
    #
    # @param LRIR  A number proportional to the distance between a wall a LRIR sensor
    # 
    # @param speed  A value from -255 to 255 that corresponds to the general 
    #               speed of the robot.
	def Follow_Wall(self, LRIR, speed = 0):
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

            print(power)

    ## Reinitialize this class to start taking data over.
    def reset(self):
        self.timer.reset()
        self.record = []


