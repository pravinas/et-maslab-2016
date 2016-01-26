import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

from tamproxy import Sketch, Timer
from tamproxy.devices import Motor, Encoder

class SerialConnect(Sketch):

    def setup(self):
        self.timer = Timer()
        # Motor object representing the left motor.
        self.leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        # Encoder object for the left motor.
        self.leftEncoder = Encoder(self.tamp, LEFT_DRIVE_ENCODER_YELLOW, LEFT_DRIVE_ENCODER_WHITE)
        # Motor object representing the right motor.
        self.rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        # Encoder object for the right motor.
        self.rightEncoder = Encoder(self.tamp, RIGHT_DRIVE_ENCODER_YELLOW, RIGHT_DRIVE_ENCODER_WHITE)

    def loop(self):
        if (self.timer.millis() > 5000):
            self.stop()

if __name__ == "__main__":
    sketch = SerialConnect()
    sketch.run()
