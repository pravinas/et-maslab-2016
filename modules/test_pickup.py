from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder, DigitalInput
from pickup import PickupModule
from constants import *

class TestPickup(SyncedSketch):

    def setup(self):
        limSwitch = DigitalInput(self.tamp, CONVEYOR_LIMIT_SWITCH)
        conveyorMotor = Motor(self.tamp, BELT_MOTOR_CONTROLLER_DIRECTION, BELT_MOTOR_CONTROLLER_PWM)
        conveyorEncoder = Encoder(self.tamp, BELT_MOTOR_ENCODER_YELLOW, BELT_MOTOR_ENCODER_WHITE)
        self.pickup = PickupModule(Timer(), Timer(), limSwitch, conveyorMotor, conveyorEncoder)
        self.pickup.start()

    def loop(self):
        response = self.pickup.run()
        if response != MODULE_PICKUP:
            self.stop()


if __name__ == "__main__":
    sketch = TestPickup(1, -0.00001, 100)
    sketch.run()