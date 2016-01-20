## constants.py

################
####  PINS  ####
################

# Main motors

RIGHT_DRIVE_CONTROLLER_DIRECTION    = 2
RIGHT_DRIVE_CONTROLLER_PWM          = 3
RIGHT_DRIVE_ENCODER_YELLOW          = 0
RIGHT_DRIVE_ENCODER_WHITE           = 1

LEFT_DRIVE_CONTROLLER_DIRECTION     = 5
LEFT_DRIVE_CONTROLLER_PWM           = 4
LEFT_DRIVE_ENCODER_YELLOW           = 29
LEFT_DRIVE_ENCODER_WHITE            = 30

BELT_MOTOR_CONTROLLER_DIRECTION     = 7
BELT_MOTOR_CONTROLLER_PWM           = 6
BELT_MOTOR_ENCODER_YELLOW           = 28
BELT_MOTOR_ENCODER_WHITE            = 27

HUGS_MOTOR_CONTROLLER_DIRECTION     = 8
HUGS_MOTOR_CONTROLLER_PWM           = 9
HUGS_MOTOR_ENCODER_YELLOW           = 26
HUGS_MOTOR_ENCODER_WHITE            = 24

# Gyro

GYRO_CS     = 10    # Chip Select
GYRO_DOUT   = 11    # MOSI - Master Output
GYRO_DIN    = 12    # MISO - Master Input
GRYO_CLOCK  = 13

# IR Sensors

LONG_DISTANCE_IR_FL  = 14
LONG_DISTANCE_IR_FR  = 15
LONG_DISTANCE_IR_BL  = 16
LONG_DISTANCE_IR_BR  = 17
SHORT_DISTANCE_IR    = 23

# Color Sensor

COLOR_SENSOR_SCL    = 18
COLOR_SENSOR_SDA    = 19

# Servo

SERVO_PIN   = 25


##########################
####  MISC CONSTANTS  ####
##########################

# Colors

RED = True
GREEN = False

# Module numbers

MODULE_FIND     = 0
MODULE_PICKUP   = 1
MODULE_DROPOFF  = 2

# The encoder count for as far as we want the encoder to move.
CONVEYOR_ENCODER_LIMIT  = 5 * 3200
# The speed of the conveyor belt. (0-255)
CONVEYOR_POWER          = 130

# The limit point at which the motor is considered stalled.
INTAKE_ENCODER_LIMIT    = 150
# The speed of the intake motors.
INTAKE_POWER            = 150

# Width of an image taken by the camera.
CAMERA_WIDTH    = 80
# Height of an image taken by the camera.
CAMERA_HEIGHT   = 60