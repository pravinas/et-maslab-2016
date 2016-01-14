# test_go_straight.py
#
# A test file for the control objects.

from go_straight import GoStraight
from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Gyro

class TestGoStraight(SyncedSketch):
    #got rid of gyro as GoStraight param to make work
    def setup(self):
        left = Motor(self.tamp, 1, 2)
        right = Motor(self.tamp, 3, 4)
        gyro = Gyro(self.tamp, 3, integrate=True)
        self.movement = GoStraight(left, right, Timer())
        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()

            # Intended behavior: Have the robot turn in a circle.
            # move_to_target() was not defined
            self.movement(90)
            
if __name__ == "__main__":
    sketch = TestGoStraight(1, -0.00001, 100)
    sketch.run()
