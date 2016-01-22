## dropoff.py
#
# Implements the DROPOFF module of the competition code.

from module import Module
from os import sys, path

from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class DropoffModule(Module):
    def __init__(self, timer, servo):
        self.timeout = 7000
        self.waitTime = 500     # Time in ms to wait for the door to actually open.
        self.openValue = 90     # Value in degrees the servo should be when the door is open.
        self.closedValue = 180  # Value in degrees the servo should be when the door is closed.
        self.timer = timer
        self.servo = servo

    ## Return True if there was an error in initialization, False otherwise.
    def checkForInitializationErrors(self):
        # TODO: Make sure servo is initialized in the "closed" position.
        return False

    ## Set up the beginning of the dropoff process.
    def start(self):
        self.timer.reset()
        self.servo.write(self.openValue)

    ## Open the back door and drive "forwards," avoiding what needs to be avoided.
    #
    # @return   The value of the next module to return to.
    def run(self):

        # Allow timeout.
        if self.timer.millis() > self.timout:
            print "Timed out from DROPOFF to FIND"
            return MODULE_FIND

        if self.timer.millis() > self.waitTime:
            # TODO: drive forward a couple inches
            self.servo.write(self.closedValue)
            raise NotImplementedError
        
        return MODULE_DROPOFF