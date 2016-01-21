from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor

UP = False
DOWN = True

class BeltMove(SyncedSketch):

    def setup(self):
        # Motor object representing the conveyor belt motor.
        self.conveyorMotor = Motor(self.tamp, 7, 6)

    def loop(self):
        self.conveyorMotor.write(DOWN, 75)

if __name__ == "__main__":
    sketch = BeltMove(1, -0.00001, 100)
    sketch.run()