from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder

# Cycles a motor back and forth between -255 and 255 PWM every ~5 seconds

# The encoder count for as far as we want the encoder to move.
CONVEYOR_ENCODER_LIMIT  = 3 * 3200
# The speed of the conveyor belt. (0-255)
CONVEYOR_POWER          = 130

UP = False
DOWN = True

class TestBelt(SyncedSketch):

    def setup(self):
        self.timer = Timer()
        self.ttt  = Timer()
        self.timeout = 5000
        # Motor object representing the conveyor belt motor.
        self.conveyorMotor = Motor(self.tamp, 7, 6)
        # Encoder object for the conveyor belt motor.
        self.conveyorEncoder = Encoder(self.tamp, 28, 27)
        self.blocksPickedUp = 0

        self.startThing()

    def loop(self):

        if self.ttt.millis() > 100:
            print self.conveyorEncoder.val
            self.ttt.reset()
        self.runThing()

    ## Set up the beginning of the pickup process.
    def startThing(self):
        self.conveyorEncoder.write(0)
        self.conveyorMotor.write(UP, CONVEYOR_POWER)
        self.timer.reset()

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def runThing(self):

        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from PICKUP to FIND"
            self.stop()

        encval = self.conveyorEncoder.val

        # Move up the conveyor belt until it hits the encoder limit.
        if encval > CONVEYOR_ENCODER_LIMIT:
            self.conveyorMotor.write(DOWN, CONVEYOR_POWER)
        else:
            self.conveyorMotor.write(UP, CONVEYOR_POWER)

        # Stop the motor when it gets to the bottom.
        if encval < 0 and self.timer.millis() > 1000:
            self.conveyorMotor.write(False, 0)
            self.blocksPickedUp += 1

            # Switch modules
            if self.blocksPickedUp >= 4:
                print "Going from PICKUP to DROPOFF"
                self.stop()
            else:
                print "Going from PICKUP to FIND"
                self.stop()
        
        return




if __name__ == "__main__":
    sketch = TestBelt(1, -0.00001, 100)
    sketch.run()