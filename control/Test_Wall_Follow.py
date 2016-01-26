# test_wall_Follow.py
#
# A test file for the control objects.

#When run returns no module named long_range_ir

from Wall_Follow import WallFollow
from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor
from long_range_ir import LRIR

class TestWallFollow(SyncedSketch):
    
    def setup(self):
        left = Motor(self.tamp, 5, 4)
        right = Motor(self.tamp, 2, 3)
        ir0 = LRIR(self.tamp,14)
        ir1 = LRIR(self.tamp,15)
        ir2 = LRIR(self.tamp,16)
        ir3 = LRIR(self.tamp,17)
        self.movement = WallFollow(left, right, Timer(), ir0, ir1, ir2, ir3)

        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()
            print self.movement.distance()

            # Intended behavior: bot will follow wall
            # IR return distance, 50 speed


            self.movement.followWall(self.movement.distance(),-35)



            
if __name__ == "__main__":
    sketch = TestWallFollow(1, -0.00001, 100)
    sketch.run()
