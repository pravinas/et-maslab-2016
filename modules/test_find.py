from tamproxy import Timer, SyncedSketch
from tamproxy.devices import Motor
from module import Module
from find import FindModule

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from control import GoStraight
from logic import Logic
from vision import Vision
from constants import *

class TestFind(SyncedSketch):

    def setup(self):
        leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        vision = Vision(RED, CAMERA_WIDTH, CAMERA_HEIGHT)
        logic = Logic()

        self.find = FindModule(Timer(), leftMotor, rightMotor, vision, logic)
        self.find.start()

    def loop(self):
        response = self.find.run()
        if response != MODULE_FIND:
            self.stop()


if __name__ == "__main__":
    sketch = TestFind(1, -0.00001, 100)
    sketch.run()