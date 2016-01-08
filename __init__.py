# __init__.py
#
# A purely syntactical file for python.
# Do not delete this file.

from ..tamproxy import SyncedSketch

class TestIR(SyncedSketch):
    def setup(self):
        self.motor1 = Motor(self.tamp, 3, 4)
        self.motor1.write(1,0)
        self.motor2 = Motor(self.tamp, 5, 6)
        self.motor2.write(1,0)
        self.delta = 1
        self.motorval = 160
        self.timer = Timer()
    
    def loop(self):
        if (self.timer.millis() > 5000):
            self.timer.reset()
            self.motorval = -self.motorval
            self.motor1.write(self.motorval>0, abs(self.motorval))
            self.motor2.write(self.motorval>0, abs(self.motorval))

if __name__ == "__main__":
    sketch = TestIR()
    sketch.run()