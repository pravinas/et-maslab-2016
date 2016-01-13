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

        # base speed for motor turning
        # 0 for turning in place
        base_speed = 0
        
        # PID is here
        # extremely simple PID controller
        # need to tweak to get propper values
        # todo
        p = 1
        i = .1
        d = .5

        
        # Will run for this amount of time before stopping
        # should be changed to stop when reaching cube/object
        # todo
        while (self.timer.millis() < 2000):

            # error value
            err = 0 - 50

            # proportional
            kp = p*err
        
            # integral/adding data points
            ki = [i*err] + ki
        
            # derivative new d*err - previous kd 
            kd = [d*err] - kd
        
            power = kp + ki + kd

            self.leftMotor.write(0,base_speed - power)
            self.rightMotor.write(1,base_speed + power)
            print("power is " + power)
            


