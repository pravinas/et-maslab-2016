from tamproxy import SyncedSketch, Timer
from tamproxy.devices import DigitalInput

class A():
	def __init__(self, switch):
		self.switch = switch

	def read(self):
		return self.switch.val

class SwitchRead(SyncedSketch):

    def setup(self):
        self.switch = A(DigitalInput(self.tamp, 21))
        self.timer = Timer()
        self.ttt = Timer()

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()
            print self.switch.read()
        if self.ttt.millis() > 8000:
        	self.stop()


if __name__ == "__main__":
    sketch = SwitchRead(1, -0.00001, 100)
    sketch.run()
