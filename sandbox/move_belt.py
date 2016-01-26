from tamproxy import SyncedSketch, Timer
from tamproxy.devices import Motor, Encoder

#Used to adjust the conveyor location

# The speed of the conveyor belt. (0-255)
CONVEYOR_POWER          = 70
INTAKE_POWER            = 120

# Used to run intake
HUGS_MOTOR_CONTROLLER_DIRECTION     = 8
HUGS_MOTOR_CONTROLLER_PWM           = 9
HUGS_MOTOR_ENCODER_YELLOW           = 26
HUGS_MOTOR_ENCODER_WHITE            = 24

class MotorWrite(SyncedSketch):

    def setup(self):
        # Motor object representing the conveyor belt motor.
        self.conveyorMotor = Motor(self.tamp, 7, 6)
        #self.intakeMotor = Motor(self.tamp, HUGS_MOTOR_CONTROLLER_DIRECTION, HUGS_MOTOR_CONTROLLER_PWM)
        self.start()

    def loop(self):
        self.conveyorMotor.write(1, CONVEYOR_POWER) #0 for up, 1 for down
        #self.intakeMotor.write(0, INTAKE_POWER) #0 for in, 1 for out


if __name__ == "__main__":
    sketch = MotorWrite(1, -0.00001, 100)
    sketch.run()