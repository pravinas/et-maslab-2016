# ColorSensor.py
# 
# Firmware for:
# https://www.adafruit.com/products/1334

class ColorSensor():

# initializes the class.
# the four variables declared correspond to the voltages of the pins for red, green, blue, and clear (colors)
    def __init__(self, clear, red, green, blue):
        self.clear = clear
        self.red = red
        self.green = green
        self.blue = blue
        # maybe add hvc things

# reads the inputs from the sensor
# saves them in the class variables
    def sense():
        pass

# true if what is being looked at is red
    def isRed():
        sense()
        if self.Red > 3: # CALIBRATE THIS WHEN WE CAN
            return True
        return False

# true if what is being looked at is green
    def isGreen():
        sense()
        if self.Green > 3: # CALIBRATE THIS WHEN WE CAN
            return True
        return False
