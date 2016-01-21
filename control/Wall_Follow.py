#Wall_Follow.py

class WallFollow():

    ## Initialize a WallFollowing.
    #
    # @param left   A Motor representing t he left motor.
    # @param right  A Motor representing the right motor.
    # @param timer  A Timer for moderating data taking.
    def __init__(self, left, right, timer):
        self.leftMotor = left
        self.rightMotor = right
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


    ## get distance value from ir sensors
    # returns distance from edge of bot to wall
    #
    # IR ordered from front right ascending spind down
    # todo

    def distance(self, IR0, IR1, IR2, IR3):

        if IR0 + IR1 < IR2 + IR3: #if right < left, wall closer on right
            return (IR0 + IR1)/2
        else:
            return -(IR2 + IR3)/2

    ## Given a distance value from distance make bot move to be 14 cm from wall.
    #
    # @param distance a number proportional to the distance between the edge of robot and wall
    #                   
    # @param speed  A value from -255 to 255 that corresponds to the general 
    #               speed of the robot.

    def move_to_target(self, distance, speed = 0):
        if self.timer.millis() > 100:
            self.timer.reset()

            # error value
            # 20 from hypotenuse of a 45,45,90
            # triangle with 14.14 long sides
            err = 20 - distance 

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
        

