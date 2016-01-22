## pickup.py
#
# Implements the PICKUP module of the competition code.

from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class PickupModule(Module):
    RAISING  = 0
    STOPPING = 1
    LOWERING = 2
    FINISHING= 3

    def __init__(self, timer, conveyorLimSwitch, conveyorMotor, conveyorEncoder):
        self.timer = timer
        self.limSwitch = conveyorLimSwitch
        self.motor = conveyorMotor
        self.encoder = conveyorEncoder
        self.encoder.write(0)

        self.encval = 0             # base encoder value when the pickup module is first called.
        self.checkTime = 100        # time in ms between checking values
        self.stopTime = 500         # time in ms for the conveyor belt to stop at the top.
        self.encmax = 5.0 * 3200    # encoder value at the top of the belt.

        self.state = RAISING
    
    ## Set up the beginning of the pickup process.
    def start(self):
        self.timer.reset()
        self.encval = self.encoder.val

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def run(self):
        if self.state == RAISING:
            raise NotImplementedError
        elif self.state == STOPPING:
            raise NotImplementedError
        elif self.state == LOWERING:
            raise NotImplementedError
        elif self.state == FINISHING:
            raise NotImplementedError
        else:
            print "Unexpected action index in PICKUP"
            return MODULE_DROPOFF