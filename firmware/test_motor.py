from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor

# Cycles a motor back and forth between -255 and 255 PWM every ~5 seconds

class MotorWrite(SyncedSketch):

    def setup(self):
        self.motor1 = Motor(self.tamp, 3, 4)
        self.motor1.write(1,0)
        self.motor2 = Motor(self.tamp, 5, 6)
        self.motor2.write(1,0)
        self.delta = 1
        self.motorval = 70
        self.timer = Timer()
        self.steps = 0

    def loop(self):
        if self.steps < 2:
            if (self.timer.millis() > 5000):
                self.timer.reset()
                self.motorval = -self.motorval
                self.motor1.write(self.motorval>0, abs(self.motorval))
                self.motor2.write(self.motorval>0, abs(self.motorval))
                self.steps += 1
        elif self.steps < 5:
            if (self.timer.millis() > 5000):
                self.timer.reset()
                self.motorval = -self.motorval
                self.motor1.write(self.motorval>0, abs(self.motorval))
                self.motor2.write(self.motorval<0, abs(self.motorval))
                self.steps += 1
        else:
            self.motor1.write(0, 0)
            self.motor2.write(0, 0)
            self.stop()


if __name__ == "__main__":
    sketch = MotorWrite(1, -0.00001, 100)
    sketch.run()