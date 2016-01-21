# test_go_straight.py
#
# A test file for the control objects.

from go_straight import GoStraight
from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Gyro

class TestGoStraight(SyncedSketch):
    
    def setup(self):
        left = Motor(self.tamp, 5, 4)
        right = Motor(self.tamp, 2, 3)
        gyro = Gyro(self.tamp, 10, integrate=True)
        self.movement = GoStraight(left, right, Timer())
        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()

            # Intended behavior: Have the robot turn in a circle.
            # move_to_target() was not defined
            self.movement.move_to_target(45, 50)
            
if __name__ == "__main__":
    sketch = TestGoStraight(1, -0.00001, 100)
    sketch.run()
