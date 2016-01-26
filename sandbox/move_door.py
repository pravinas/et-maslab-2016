from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder, Servo

#Used to adjust the door



class moveDoor(SyncedSketch):

    def setup(self):
        # Servo object representing the door.
        self.openValue = 100     # Value in degrees the servo should be when the door is open.
        self.closedValue = 172  # Value in degrees the servo should be when the door is closed.

        self.servo = Servo(self.tamp, 25)
        self.start()

    def loop(self):
        # COMMENT 1 OF THESE
        #self.servo.write(self.openValue) # Use to open door
        self.servo.write(self.closedValue) # Use to close door


if __name__ == "__main__":
    sketch = moveDoor(1, -0.00001, 100)
    sketch.run()