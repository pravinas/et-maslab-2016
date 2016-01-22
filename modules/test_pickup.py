from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder
from pickup import PickupModule

MODULE_PICKUP = 1

class TestPickup(SyncedSketch):

    def setup(self):
        limSwitch = None
        conveyorMotor = Motor(self.tamp, 7, 6)
        conveyorEncoder = Encoder(self.tamp, 28, 27)
        self.pickup = Pickup(Timer(), limSwitch, conveyorMotor, conveyorEncoder)
        self.pickup.start()

    def loop(self):
        response = self.pickup.run()
        if response != MODULE_PICKUP
            self.stop()


if __name__ == "__main__":
    sketch = TestPickup(1, -0.00001, 100)
    sketch.run()