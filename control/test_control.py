# test_control.py
# 
# Run a sketch that tells the robot to run various control routines.

import tamproxy
from ..firmware.short_range_ir import IR

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

    # using two IR seonsors moving 13cm approx 5in from wall
    # made assuming both sensors are at right side 
    # motor1 = left
    # motor2 = right  
    # todo

    def loop(self):
        # assuming numbered IR sensors spin down from front 0,1,2,4
        # assuming following right wall
        if (self.timer.millis() > 10):
            self.timer.reset()
    
            if IR0 < 15:
            # IR values will be in cm
            # todo
                self.motor1.write(0, 50 )
                self.motor2.write(1, 50 + 25)

            elif IR0 > 15:
            # makes motor 1 faster for some value
            # turn left closer to wall
            #todo
                self.motor1.write(0, 50 + 25)
                self.motor2.write(1, 50)
            else:
            # goes forward
            #todo
                self.motor1.write(0, 50)
                self.motor2.write(1, 50)

        