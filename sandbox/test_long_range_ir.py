# test_long_range_ir.py
#
# A sketch to test and calibrate the IR sensor.

from tamproxy import SyncedSketch, Timer
from long_range_ir import LRIR

class TestIRBR(SyncedSketch):
    def setup(self):
        self.ir = LRIR(self.tamp, 15)
        self.sum = 0
        self.timer = Timer()
        self.timestep = 0

    def loop(self):
        if (self.timer.millis() > 1000):
            self.timer.reset()
            #self.sum += self.ir.read_ir()
            self.timestep += 1
            print self.timestep
            raw = self.ir.val
            print "raw val:",raw
            print "distance:",self.convertToDistance(raw)
            #print "average:",self.sum / self.timestep

    ## Takes raw IR data and outputs centimeters
    def convertToDistance(self, raw):
        return (1.0/raw)*799400-9.119

if __name__ == "__main__":
    sketch = TestIRBR(1, -0.00001, 100)
    sketch.run()