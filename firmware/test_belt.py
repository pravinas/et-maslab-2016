from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder

# Cycles a motor back and forth between -255 and 255 PWM every ~5 seconds

# The encoder count for as far as we want the encoder to move.
CONVEYOR_ENCODER_LIMIT  = 5 * 3200
# The speed of the conveyor belt. (0-255)
CONVEYOR_POWER          = 130

class MotorWrite(SyncedSketch):

    def setup(self):
        self.timer = Timer()
        self.timeout = 7000
        # Motor object representing the conveyor belt motor.
        self.conveyorMotor = Motor(self.tamp, 7, 6)
        # Encoder object for the conveyor belt motor.
        self.conveyorEncoder = Encoder(self.tamp, 28, 27)
        self.blocksPickedUp = 0

        self.start()

    def loop(self):
        if self.timer.millis() > 8000:
            self.motor1.write(0, self.motorval) #0 for up, 1 for down
        if self.timer.millis() > 14000:
            self.motor1.write(1, 0)
            self.stop()

    ## Set up the beginning of the pickup process.
    def start(self):
        print self.conveyorEncoder.val
        self.run()

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def run(self):

        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from PICKUP to FIND"
            self.stop()

        encval = self.conveyorEncoder.val

        # Move up the conveyor belt until it hits the encoder limit.
        if encval > CONVEYOR_ENCODER_LIMIT:
            self.conveyorMotor.write(True, CONVEYOR_POWER)
        else:
            self.conveyorMotor.write(False, CONVEYOR_POWER)

        # Stop the motor when it gets to the bottom.
        if encval < 0 and self.timer.millis() > 200:
            self.conveyorMotor.write(False, 0)
            self.blocksPickedUp += 1

            # Switch modules
            if self.blocksPickedUp >= 4:
                print "Going from PICKUP to DROPOFF"
                self.stop()
            else:
                print "Going from PICKUP to FIND"
                self.stop()
        
        return MODULE_PICKUP




if __name__ == "__main__":
    sketch = MotorWrite(1, -0.00001, 100)
    sketch.run()