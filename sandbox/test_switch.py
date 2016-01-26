from tamproxy import SyncedSketch, Timer
from tamproxy.devices import DigitalInput

class SwitchRead(SyncedSketch):

    def setup(self):
        self.switch = DigitalInput(self.tamp, 23)
        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()
            print self.switch.val


if __name__ == "__main__":
    sketch = SwitchRead(1, -0.00001, 100)
    sketch.run()
