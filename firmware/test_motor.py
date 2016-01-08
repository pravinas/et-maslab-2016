from tamproxy import Sketch, SyncedSketch, Timer
from tamproxy.devices import Motor

# Cycles a motor back and forth between -255 and 255 PWM every ~5 seconds

class MotorWrite(Sketch):

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
    sketch = MotorWrite()
    sketch.run()