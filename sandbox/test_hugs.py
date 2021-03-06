from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder

# Cycles a motor back and forth between -255 and 255 PWM every ~5 seconds

HUGS_MOTOR_CONTROLLER_DIRECTION     = 8
HUGS_MOTOR_CONTROLLER_PWM           = 9
HUGS_MOTOR_ENCODER_YELLOW           = 31
HUGS_MOTOR_ENCODER_WHITE            = 32

# The limit point at which the motor is considered stalled.
INTAKE_ENCODER_LIMIT    = 150
# The speed of the intake motors.
INTAKE_POWER            = 120

class HugTest(SyncedSketch):

    def setup(self):
        # Motor object representing the intake mechanism motors.
        self.intakeMotor = Motor(self.tamp, HUGS_MOTOR_CONTROLLER_DIRECTION, HUGS_MOTOR_CONTROLLER_PWM)
        # Encoder object for the intake motor.
        self.intakeEncoder = Encoder(self.tamp, HUGS_MOTOR_ENCODER_YELLOW, HUGS_MOTOR_ENCODER_WHITE)
        # Timer object to moderate checking for intake errors.
        self.intakeTimer = Timer()
        # Are the intake motors going forward? True if so, False if reversing.
        self.intakeDirection = False
        # Start the intake motor.
        self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)

    def loop(self):
        self.checkForIntakeErrors()

    def checkForIntakeErrors(self, checkTime = 1000, reverseTime = 3000):

        if self.intakeDirection:    # We are moving forward.
            if self.intakeTimer.millis() > checkTime:
                self.intakeTimer.reset()
                if self.intakeEncoder.val < INTAKE_ENCODER_LIMIT: # if we're stalled
                    self.intakeDirection = True
                    self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)
                else: # if we're not stalled
                    self.intakeEncoder.write(0)

        else:                       # We are reversing the motors.
            if self.intakeTimer.millis() > reverseTime:
                self.intakeTimer.reset()
                self.intakeDirection = False
                self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)
                self.intakeEncoder.write(0)

        self.intakeMotor.write(self.intakeDirection, INTAKE_POWER)

if __name__ == "__main__":
    sketch = HugTest(1, -0.00001, 100)
    sketch.run()