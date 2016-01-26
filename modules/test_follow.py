from tamproxy import Timer, SyncedSketch
from tamproxy.devices import Motor, Color, Encoder
from module import Module
from follow import FollowModule
from control.long_range_ir import LRIR
from logic import Logic
from constants import *

class TestFind(SyncedSketch):

    def setup(self):
        timer = Timer()
        timeoutTimer = Timer()
        leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        irBL = LRIR(self.tamp, LONG_DISTANCE_IR_BL)
        irBR = LRIR(self.tamp, LONG_DISTANCE_IR_BR)
        irFL = LRIR(self.tamp, LONG_DISTANCE_IR_FL)
        irFR = LRIR(self.tamp, LONG_DISTANCE_IR_FR)
        forwardSpeed = 50
        logic = Logic()

        self.follow = FollowModule(timer, timeoutTimer, leftMotor, rightMotor, irBL, irBR, irFL, irFR, forwardSpeed, logic)
        self.follow.start()

    def loop(self):
        response = self.follow.run()
        if response != MODULE_FOLLOW:
            self.stop()


if __name__ == "__main__":
    sketch = TestFind(1, -0.00001, 100)
    sketch.run()