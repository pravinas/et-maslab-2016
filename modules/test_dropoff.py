from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder, Servo
from dropoff import DropoffModule
from constants import *


class TestDropoff(SyncedSketch):

    def setup(self):
        self.ttt = Timer()
        self.timer = Timer()
        self.loopTimer = Timer()
        self.servo = Servo(self.tamp, SERVO_PIN)

        self.motorRight = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        self.motorLeft = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        self.encoder = Encoder(self.tamp, RIGHT_DRIVE_ENCODER_YELLOW, RIGHT_DRIVE_ENCODER_WHITE)

        self.dropoff = DropoffModule(self.timer, self.servo, self.motorRight, self.motorLeft, self.encoder)
        self.dropoff.start()

    def loop(self):
        if self.ttt.millis() > 100:
            self.ttt.reset()
            response = self.dropoff.run()
            if response != MODULE_DROPOFF:
                self.stop()




if __name__ == "__main__":
    sketch = TestDropoff(1, -0.00001, 100)
    sketch.run()