# test_wall_Follow.py
#
# A test file for the control objects.

#When run returns no module named long_range_ir

from Wall_Follow import WallFollow
from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor
from long_range_ir import LRIR
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *


class TestWallFollow(SyncedSketch):
    
    def setup(self):
        self.left = Motor(self.tamp, 5, 4)
        self.right = Motor(self.tamp, 2, 3)
        hugs = Motor(self.tamp, 8, 9)
        ir0 = LRIR(self.tamp,14)
        ir1 = LRIR(self.tamp,15)
        ir2 = LRIR(self.tamp,16)
        ir3 = LRIR(self.tamp,17)
        self.movement = WallFollow(self.left, self.right, Timer(), ir0, ir1, ir2, ir3)

        self.timer = Timer()
        self.wintimer = Timer()

    def loop(self):
        if self.wintimer.millis() < 19600:
            if self.timer.millis() > 100:
                self.timer.reset()
                print self.movement.distance()

            # Intended behavior: bot will follow wall
            # IR return distance, 50 speed


                self.movement.followWall(self.movement.distance(),-FORWARD_SPEED)
        elif self.wintimer.millis() < 19900:
            self.left.write( 0, 145)
            self.right.write( 1, 145)
        else:
            self.wintimer.reset()
            self.left.write(0,0)
            self.right.write(0,0)



            
if __name__ == "__main__":
    sketch = TestWallFollow(1, -0.00001, 100)
    sketch.run()
