from tamproxy import Sketch, SyncedSketch, Timer
from tamproxy.devices import Servo


class ServoWrite(Sketch):
    """Cycles a servo back and forth between 1050us and 1950us pulse widths (most servos are 1000-2000)"""

    def setup(self):
        self.servo = Servo(self.tamp, 18)
        self.servo.write(1050)
        self.timer = Timer()
        self.fulltime = Timer()
        self.end = False

    def loop(self):
        if (self.timer.millis() > 2000):
            self.timer.reset()
            if self.end:
                self.servo.write(1050)
            else:
                self.servo.write(1950)
            self.end = not self.end
        if self.fulltime > 20000:
            self.stop()
            
    def stop(self):
        super(EncoderRead,self).stop()
        self.tamp.clear_devices()

if __name__ == "__main__":
    sketch = ServoWrite()
    sketch.run()