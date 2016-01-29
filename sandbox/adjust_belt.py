from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, DigitalInput

UP = False
DOWN = True

class BeltMove(SyncedSketch):

    def setup(self):
        # Motor object representing the conveyor belt motor.
        self.limSwitch = DigitalInput(self.tamp, 23)
        self.conveyorMotor = Motor(self.tamp, 7, 6)
        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 100:
        	self.timer.reset()
	    	if self.limSwitch.val:
	    		self.conveyorMotor.write(UP, 0)
                        self.stop()
	    	else:
	    		self.conveyorMotor.write(DOWN, 80)

if __name__ == "__main__":
    sketch = BeltMove(1, -0.00001, 100)
    sketch.run()
