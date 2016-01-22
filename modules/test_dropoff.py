from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder

RIGHT_DRIVE_CONTROLLER_DIRECTION    = 2
RIGHT_DRIVE_CONTROLLER_PWM          = 3

LEFT_DRIVE_CONTROLLER_DIRECTION     = 5
LEFT_DRIVE_CONTROLLER_PWM           = 4

SERVO_PIN   = 25

MODULE_FIND     = 0

FORWARD_SPEED = 70

class TestDropoff(SyncedSketch):

    def setup(self):
        self.timeout = 7000
        self.waitTime = 500     # Time in ms to wait for the door to actually open.
        self.openValue = 90     # Value in degrees the servo should be when the door is open.
        self.closedValue = 180  # Value in degrees the servo should be when the door is closed.
        self.timer = Timer()
        self.servo = Servo(self.tamp, SERVO_PIN)

        self.motorRight = Motor(self.tamp, RIGHT_DRIVE_CONTROLLER_DIRECTION, RIGHT_DRIVE_CONTROLLER_PWM)
        self.motorRight.write(1,0)
        self.motorLeft = Motor(self.tamp, LEFT_DRIVE_CONTROLLER_DIRECTION, LEFT_DRIVE_CONTROLLER_PWM)
        self.motorLeft.write(1,0)

        self.doorTimer = doorTimer

        self.startThing()

    def loop(self):
        self.runThing()

    ## Set up the beginning of the pickup process.
    def startThing(self):
        # TODO: Make sure that the cube drop-off location is actually good
        self.timer.reset()
        self.servo.write(self.openValue)

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def runThing(self):   
        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from DROPOFF to FIND"
            return MODULE_FIND

        # After Door opens, go forward
        if self.timer.millis() > self.waitTime:
            self.doorTimer.reset()
            self.motorRight.write(0,FORWARD_SPEED)
            self.motorLeft.write(0,FORWARD_SPEED)

            # After robot moves forward enough, stop moving and close the door
            if self.doorTimer.millis() > 3000:
                self.motorRight.write(0,0)
                self.motorLeft.write(0,0)
                self.servo.write(self.closedValue)
                return MODULE_DROPOFF
        
        return MODULE_DROPOFF




if __name__ == "__main__":
    sketch = TestDropoff(1, -0.00001, 100)
    sketch.run()