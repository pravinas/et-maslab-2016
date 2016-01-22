## pickup.py
#
# Implements the PICKUP module of the competition code.

from module import Module
from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class PickupModule(Module):
    def __init__(self, timer, conveyorMotor, conveyorEncoder):
        self.timer = timer
        self.timeout = 7000
        self.conveyorMotor = conveyorMotor
        self.conveyorEncoder = conveyorEncoder
        self.blocksPickedUp = 0

    ## Return True if there was an error in initialization, False otherwise.
    def checkForInitializationErrors(self):
        return False
    
    ## Set up the beginning of the pickup process.
    def start(self):
        self.conveyorEncoder.write(0)
        self.conveyorMotor.write(True, CONVEYOR_POWER)
        self.timer.reset()

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def run(self):

        # Allow timeout.
        if self.timer.millis() > self.timeout:
            print "Timed out from PICKUP to FIND"
            return MODULE_FIND

        encval = self.conveyorEncoder.val

        # Move up the conveyor belt until it hits the encoder limit.
        if encval > CONVEYOR_ENCODER_LIMIT:
            self.conveyorMotor.write(True, CONVEYOR_POWER)
        else:
            self.conveyorMotor.write(False, CONVEYOR_POWER)

        # Stop the motor when it gets to the bottom.
        if encval < 0 and self.timer.millis() > 200:
            self.conveyorMotor.write(False, 0)
            self.blocksPickedUp += 1

            # Switch modules
            if self.blocksPickedUp >= 4:
                print "Going from PICKUP to DROPOFF"
                return MODULE_DROPOFF
            else:
                print "Going from PICKUP to FIND"
                return MODULE_FIND
        
        return MODULE_PICKUP
