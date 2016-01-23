# test_wall_Follow.py
#
# A test file for the control objects.

#When run returns no module named long_range_ir

from Wall_Follow import followWall
from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor

class TestWallFollow(SyncedSketch):
    
    def setup(self):
        left = Motor(self.tamp, 5, 4)
        right = Motor(self.tamp, 2, 3)
        self.movement = WallFollow(left, right, Timer())
        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()

            # Intended behavior: bot will slowly turn right
            # 51 distance, 50 speed

            self.movement.followWall(51,50)



            
if __name__ == "__main__":
    sketch = WallFollow(1, -0.00001, 100)
    sketch.run()
