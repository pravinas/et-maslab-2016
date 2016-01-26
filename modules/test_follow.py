import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tamproxy import Timer, SyncedSketch
from tamproxy.devices import Motor, Color, Encoder
from follow import FollowModule
from control.long_range_ir import LRIR
from logic import Logic
from vision import Vision
from constants import *

class TestFollow(SyncedSketch):

    def setup(self):
        timer = Timer()
        timeoutTimer = Timer()
        leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        irBL = LRIR(self.tamp, LONG_DISTANCE_IR_BL)
        irBR = LRIR(self.tamp, LONG_DISTANCE_IR_BR)
        irFL = LRIR(self.tamp, LONG_DISTANCE_IR_FL)
        irFR = LRIR(self.tamp, LONG_DISTANCE_IR_FR)
        forwardSpeed = -50
        logic = Logic()
        vision = Vision(True, CAMERA_WIDTH, CAMERA_HEIGHT, debug=True)

        self.follow = FollowModule(timer, timeoutTimer, leftMotor, rightMotor, irBL, irBR, irFL, irFR, forwardSpeed, logic, vision)
        self.follow.start()

    def loop(self):
        response = self.follow.run()
        if response != MODULE_FOLLOW:
            self.stop()


if __name__ == "__main__":
    sketch = TestFollow(1, -0.00001, 100)
    sketch.run()