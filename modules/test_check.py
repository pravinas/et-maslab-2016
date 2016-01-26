from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Color
from check import CheckModule

class TestCheck(SyncedSketch):

    def setup(self):
        timer = Timer()
        timeoutTimer = Timer()
        leftMotor = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        rightMotor = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        intakeMotor = Motor(self.tamp, HUGS_DRIVE_CONTROLLER_DIRECTION, HUGS_DRIVE_CONTROLLER_PWM)
        color = Color(self.tamp)
        self.check = CheckModule(timer, timeoutTimer, leftMotor, rightMotor, intakeMotor, color)
        self.check.start()

    def loop(self):
        response = self.check.run()
        if response != MODULE_CHECK:
            self.stop()


if __name__ == "__main__":
    sketch = TestCheck(1, -0.00001, 100)
    sketch.run()