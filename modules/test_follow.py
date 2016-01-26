import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tamproxy import Timer, SyncedSketch
from tamproxy.devices import Motor, DigitalInput
from follow import FollowModule
from control.long_range_ir import LRIR
from control.Wall_Follow import WallFollow
from constants import *

class TestFollow(SyncedSketch):

    def setup(self):
        timer = Timer()
        stepTimer = Timer()
        wallFollowTimer = Timer()
        leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        irFL = LRIR(self.tamp, LONG_DISTANCE_IR_FL)
        irFR = LRIR(self.tamp, LONG_DISTANCE_IR_FR)
        irBL = LRIR(self.tamp, LONG_DISTANCE_IR_BL)
        irBR = LRIR(self.tamp, LONG_DISTANCE_IR_BR)
        wallFollow = WallFollow(leftMotor, rightMotor, wallFollowTimer, irFL, irFR, irBL, irBR)
        blockSwitch = DigitalInput(self.tamp, BLOCK_LIMIT_SWITCH)
        self.follow = FollowModule(timer, stepTimer, leftMotor, rightMotor, wallFollow, FORWARD_SPEED, blockSwitch)
        self.follow.start()

    def loop(self):
        response = self.follow.run()
        if response != MODULE_FOLLOW:
            self.stop()


if __name__ == "__main__":
    sketch = TestFollow(1, -0.00001, 100)
    sketch.run()