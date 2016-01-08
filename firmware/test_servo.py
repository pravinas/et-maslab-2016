# test_servo.py
#
# A sketch to test the servo.

from tamproxy import SyncedSketch, Timer
from tamproxy.devices import AnalogOutput

class TestServo(SyncedSketch):
    def setup(self):
        self.servo = AnalogOutput(self.tamp, 23)
        self.timer = Timer()
        self.exper = [2.5,0]
        self.times = 0

    def loop(self):
        if self.timer.millis() > 2000:
            self.timer.reset()
            print self.exper[self.times]
            self.servo.write(self.exper[self.times])
            self.times += 1
        if self.times >= len(self.exper):
            self.stop()

if __name__ == "__main__":
    sketch = TestServo(1, -0.00001, 100)
    sketch.run()