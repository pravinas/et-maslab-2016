from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor

# Cycles a motor back and forth between -255 and 255 PWM every ~5 seconds

class MotorWrite(SyncedSketch):

    def setup(self):
        self.motor1 = Motor(self.tamp, 7, 6)
        self.motorval = 100
        self.motor1.write(0,self.motorval)
        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 8000:
            self.motor1.write(1, self.motorval)
        if self.timer.millis() > 14000:
            self.motor1.write(1, 0)
            self.stop()

if __name__ == "__main__":
    sketch = MotorWrite(1, -0.00001, 100)
    sketch.run()