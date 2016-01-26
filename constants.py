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
#### MODULE CONSTANTS ####
##########################

############
## Pickup ##
############

# time in ms for the conveyor belt to stop at the top.
PICKUP_STOP_TIME        = 500
# Number of rotations for the conveyor belt motor to make.
PICKUP_NUM_ROTATIONS    = 5.1
# encoder value at the top of the belt.
PICKUP_ENCODER_MAX      = PICKUP_NUM_ROTATIONS * 3200
# Power to drive the conveyor belt.
PICKUP_CONVEYOR_POWER   = 130
# Direction for belt to go up
PICKUP_BELT_UP          = False
# Direction for belt to go down
PICKUP_BELT_DOWN        = True
# Timeout for entire pickup module
PICKUP_TIMEOUT          = 15000
# The most blocks that the robot can handle
PICKUP_MAX_BLOCKS       = 4

# Pickup internal state machine
PICKUP_RAISING  = 0
PICKUP_STOPPING = 1
PICKUP_LOWERING = 2


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

# Intake directions
INTAKE_IN = 0
INTAKE_OUT = 1

# Width of an image taken by the camera.
CAMERA_WIDTH    = 80
# Height of an image taken by the camera.
CAMERA_HEIGHT   = 60

# Distance between wheels in inches.
WHEEL_WIDTH = 12

# Default speed for going forward
FORWARD_SPEED = 50

# Motor Drive Directions
FORWARD_DIR = 0
BACKWARD_DIR = 1

#Desired distance between IR and wall
WALL_DISTANCE = 40

# Value in degrees the servo should be when the door is open.
SERVO_OPEN  = 100
# Value in degrees the servo should be when the door is closed.
SERVO_CLOSE = 172