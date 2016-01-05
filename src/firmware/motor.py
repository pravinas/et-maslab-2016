# motor.py
# 
# Firmware for:
# 50:1 Metal Gearmotor 37Dx70L mm with 64 CPR Encoder

class Motor():

    ## Initialize a Motor object with pin numbers.
    #
    # @param red    The analog pin that the red wire connects to.
    #               Controls voltage to one terminal of the motor.
    # @param black  The analog pin that the black wire connects to.
    #               Controls voltage to the other terminal.
    # @param green  The ground pin (for the encoder).
    # @param blue   Encoder Vcc. Ideally 12V, can be 3.5V - 20V.
    # @param yellow Encoder A output. Squarewave T = Rotation/16.
    # @param white  Encoder B output. Squarewave T = Rotation/16.
    #               90 deg out of phase with output A.
    def __init__(self, red, black, green, blue, yellow, white):
        self.red = red
        self.black = black
        self.green = green
        self.blue = blue
        self.yellow = yellow
        self.white = white
