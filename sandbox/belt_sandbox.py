from tamproxy import Sketch, SyncedSketch, Timer
from tamproxy.devices import Encoder, Motor

UP = False
DOWN = True

# Prints a quadrature encoder's position
class EncoderRead(SyncedSketch):

    def setup(self):
        self.steps = 0
        # Motor object representing the conveyor belt motor.
        self.motor = Motor(self.tamp, 7, 6)
        # Encoder object for the conveyor belt motor.
        self.encoder = Encoder(self.tamp, 28, 27)
        self.timer = Timer()
        self.motor.write(DOWN, 75)

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()
            self.steps += 1
            print self.steps, self.encoder.val
        if self.steps > 25:
            self.motor.write(DOWN, 75)
            self.stop()

if __name__ == "__main__":
    sketch = EncoderRead(1, -0.00001, 100)
    sketch.run()
