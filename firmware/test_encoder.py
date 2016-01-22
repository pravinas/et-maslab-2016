from tamproxy import Sketch, SyncedSketch, Timer
from tamproxy.devices import Encoder, Motor


class EncoderRead(SyncedSketch):

    encoderPins = 28, 27
    motorPwm = 6 #green
    motorDir = 7 #yellow

    def setup(self):
        self.encoder = Encoder(self.tamp, *self.encoderPins, continuous=True)
        self.motor = Motor(self.tamp, self.motorDir, self.motorPwm)
        self.miscTimer = Timer()
        self.timer = Timer()
        self.rotations = 0
        self.lastRot = 0
        self.motor.write(0, 100)

    def loop(self):
        if self.timer.millis() > 100:
            print "enc", self.encoder.val
            self.timer.reset()
        if self.encoder.val > 5.0 * 3200:
            print "Stopped at", self.encoder.val
            self.motor.write(1,0)
            self.stop()

        '''
        if abs(self.encoder.val) > 3200 and self.timer.millis() > self.lastRot + 50:
            self.rotations += 1
            print "~~~~~~~~~~~"
            print "Rotation", self.rotations
            print "Encoder Val", self.encoder.val
            print "Time", self.timer.millis()
            print "~~~~~~~~~~~"
            self.encoder.write(0)
            self.motor.write(1,0)
            self.lastRot = self.timer.millis()

        if self.miscTimer.millis() > 1000:
            self.miscTimer.reset()
            self.motor.write(0,100)

        if self.rotations > 5:
            self.motor.write(1,0)
            self.stop()
        '''

if __name__ == "__main__":
    sketch = EncoderRead(1, -0.00001, 100)
    sketch.run()