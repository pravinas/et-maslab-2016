# test_short_range_ir.py
#
# A sketch to test and calibrate the IR sensor.

from tamproxy import SyncedSketch, Timer
from short_range_ir import IR

class TestIR(SyncedSketch):
    def setup(self):
        self.ir = IR(self.tamp, 23)
        self.sum = 0
        self.timer = Timer()
        self.timestep = 0

    def loop(self):
        if (self.timer.millis() > 100):
            self.timer.reset()
            #self.sum += self.ir.read_ir()
            self.timestep += 1
            print self.timestep
            print "raw val:",self.ir.val
            print "distance:",self.ir.read_ir()
            #print "average:",self.sum / self.timestep

if __name__ == "__main__":
    sketch = TestIR(1, -0.00001, 100)
    sketch.run()