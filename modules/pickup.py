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

    BELT_UP = False
    BELT_DOWN = True

    def __init__(self, timer, conveyorLimSwitch, conveyorMotor, conveyorEncoder):
        self.timer = timer
        self.limSwitch = conveyorLimSwitch
        self.motor = conveyorMotor
        self.encoder = conveyorEncoder
        self.encoder.write(0)

        self.encval = 0             # base encoder value when the pickup module is first called.
        self.stopTime = 500         # time in ms for the conveyor belt to stop at the top.
        self.stopT = 0              # time at which the belt stops.
        self.encmax = 5.0 * 3200    # encoder value at the top of the belt.
        self.power = 130            # power at which to drive motors.

        self.blocksCollected = 0

    
    ## Set up the beginning of the pickup process.
    def start(self):
        self.timer.reset()
        self.encval = self.encoder.val
        self.motor.write(self.BELT_UP, self.power)
        self.state = self.RAISING
        print "RAISING"

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def run(self):
        if self.state == self.RAISING:
            # Check every timestep whether self.encoder.val > self.encval
            if self.encoder.val > self.encval + self.encmax:
                self.state = self.STOPPING
                self.stopT = self.timer.millis()
                print "STOPPING at t =", self.stopT

        elif self.state == self.STOPPING:
            # Stop for a short time
            if self.timer.millis() > self.stopT + self.stopTime:
                self.state = self.LOWERING
                self.motor.write(self.DOWN, self.power)
                self.blocksCollected += 1
                print "LOWERING with", self.blocksCollected, "blocks inside"

        elif self.state == self.LOWERING:
            # TODO: Take limswitch into account. Shouldn't be hard?
            if self.encoder.val < self.encval:
                self.motor.write(0,0)
                if self.blocksCollected >= 4:
                    print "Going from PICKUP to DROPOFF"
                    self.blocksCollected = 0
                    return MODULE_DROPOFF
                else:
                    print "Going from PICKUP to FIND"
                    return MODULE_FIND

        else:
            print "Unexpected action index in PICKUP"
            self.blocksCollected = 0
            return MODULE_DROPOFF

        return MODULE_PICKUP