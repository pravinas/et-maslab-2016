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
BELT_MOTOR_ENCODER_YELLOW           = 31
BELT_MOTOR_ENCODER_WHITE            = 32

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

# Color Sensor

COLOR_SENSOR_SCL    = 18
COLOR_SENSOR_SDA    = 19

# Servo
SERVO_PIN   = 25

# Limit Switches
BLOCK_LIMIT_SWITCH      = 21
CONVEYOR_LIMIT_SWITCH   = 22

# Competition Mode
COMPETITION_MODE    = 23

##########################
####  MISC CONSTANTS  ####
##########################

# Colors: The one that is our color should be True, and the other False.

RED     = True
GREEN   = False

# Module numbers

MODULE_CHECK    = 0
MODULE_PICKUP   = 1
MODULE_DROPOFF  = 2
MODULE_FOLLOW   = 3

# The limit point at which the motor is considered stalled.
INTAKE_ENCODER_LIMIT    = 150
# The speed of the intake motors. (0-255)
INTAKE_POWER            = 120

# Width of an image taken by the camera.
CAMERA_WIDTH    = 80
# Height of an image taken by the camera.
CAMERA_HEIGHT   = 60

# Distance between wheels in inches.
WHEEL_WIDTH = 12

#D efault speed for going forward
FORWARD_SPEED = 50

#Desired distance between IR and wall
WALL_DISTANCE = 40

# Value in degrees the servo should be when the door is open.
SERVO_OPEN  = 100
# Value in degrees the servo should be when the door is closed.
SERVO_CLOSE = 172