# ColorSensor.py
# 
# Firmware for:
# https://www.adafruit.com/products/1334

class ColorSensor():

    ## Initializes the class with pin number inputs.
    #
    # @param clear  The pin number of the clear voltage input.
    # @param red    The pin number of the red voltage input.
    # @param green  The pin number of the green voltage input.
    # @param blue   The pni number of the blue voltage input.
    def __init__(self, clear, red, green, blue):
        self.clear = clear
        self.red = red
        self.green = green
        self.blue = blue
        # maybe add hsv things

    ## Reads the inputs from the sensor
    # 
    # @return A tuple of voltages from the pins.
    def sense(self):
        pass

    ## Tell if the color is in fact sensing red.
    #
    # @return true if what is being looked at is red.
    #              false otherwise
    def isRed(self):
        clear, red, green, blue = self.sense()
        if red > 3: # TODO: CALIBRATE THIS WHEN WE CAN
            return True
        return False


    ## Tell if the color is in fact sensing green.
    #
    # @return true if what is being looked at is green.
    #              false otherwise
    def isGreen(self):
        clear, red, green, blue = self.sense()
        if green > 3: # TODO: CALIBRATE THIS WHEN WE CAN
            return True
        return False
