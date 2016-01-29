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
PICKUP_STOP_TIME        		= 500
# Number of rotations for the conveyor belt motor to make.
PICKUP_NUM_ROTATIONS    		= 5.2
# encoder value at the top of the belt.
PICKUP_ENCODER_MAX      		= PICKUP_NUM_ROTATIONS * 3200
# Power to drive the conveyor belt up.
PICKUP_CONVEYOR_POWER_RAISE		= 130
# Power to drive the conveyor belt down.
PICKUP_CONVEYOR_POWER_LOWER		= 130
# Direction for belt to go up
PICKUP_BELT_UP          		= False
# Direction for belt to go down
PICKUP_BELT_DOWN        		= True
# Timeout for entire pickup module
PICKUP_TIMEOUT          		= 15000
# The most blocks that the robot can handle
PICKUP_MAX_BLOCKS       		= 7

# Pickup internal state machine
PICKUP_RAISING  = 0
PICKUP_STOPPING = 1
PICKUP_LOWERING = 2

#############
## Dropoff ##
#############

# Timeout for entire dropoff module
DROPOFF_TIMEOUT		= 2000
# Time in ms to wait for the door to actually open.
DROPOFF_WAIT_TIME	= 500
# Encoder value when needing to stop
DROPOFF_ENC_MAX		= 2500

############
## Follow ##
############

# Time in ms to follow the wall
FOLLOW_WALL_TIME = 7000
# Timestamp at which to stop turning
FOLLOW_TURN_TIME = FOLLOW_WALL_TIME + 500

###########
## Check ##
###########

# Time in ms to run the intakes backwards for an incorrect block.
CHECK_SPIT_TIME = 500
# Timestamp at which to stop turning
CHECK_TURN_TIME = CHECK_SPIT_TIME + 500

##########################
####  MISC CONSTANTS  ####
##########################

# Colors: The one that is our color should be True, and the other False.

RED     = True
GREEN   = False

# Module numbers

MODULE_END		= -1
MODULE_OFF      = 0
MODULE_FOLLOW   = 1
MODULE_CHECK    = 2
MODULE_PICKUP   = 3
MODULE_DROPOFF  = 4

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

# Speed for turning suddenly
TURN_FAST_SPEED = 145

# Motor Drive Directions
FORWARD_DIR = 0
BACKWARD_DIR = 1

#Desired distance between IR and wall
WALL_DISTANCE = 30

# Value in degrees the servo should be when the door is open.
SERVO_OPEN  = 100
# Value in degrees the servo should be when the door is closed.
SERVO_CLOSE = 172

# Length of game in ms.
GAME_LENGTH = 180000
