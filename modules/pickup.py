## pickup.py
#
# Implements the PICKUP module of the competition code.

from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class PickupModule(Module):

    def __init__(self, timer, conveyorLimSwitch, conveyorMotor, conveyorEncoder):
        self.timer = timer
        self.limSwitch = conveyorLimSwitch
        self.motor = conveyorMotor
        self.encoder = conveyorEncoder
        self.encoder.write(0)

        self.encval = 0             # base encoder value when the pickup module is first called.
        self.stopTime = 0           # time at which the belt stops.
        self.blocksCollected = 0

    
    ## Set up the beginning of the pickup process.
    def start(self):
        self.timer.reset()
        self.encval = self.encoder.val
        self.motor.write(PICKUP_BELT_UP, PICKUP_CONVEYOR_POWER)
        self.state = PICKUP_RAISING
        print "RAISING"

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def run(self):
        if self.timer.millis() > PICKUP_TIMEOUT:
            if self.blocksCollected >= PICKUP_MAX_BLOCKS:
                print "Timed out from PICKUP to DROPOFF"
                self.blocksCollected = 0
                return MODULE_DROPOFF
            else:
                print "Timed out from PICKUP to FIND"
                return MODULE_FOLLOW

        if self.state == PICKUP_RAISING:
            # Check every timestep whether self.encoder.val > self.encval
            if self.encoder.val > self.encval + PICKUP_ENCODER_MAX:
                self.state = PICKUP_STOPPING
                self.motor.write(0,0)
                self.stopTime = self.timer.millis()
                print "STOPPING at t =", self.stopTime

        elif self.state == PICKUP_STOPPING:
            # Stop for a short time
            if self.timer.millis() > self.stopTime + PICKUP_STOP_TIME:
                self.state = PICKUP_LOWERING
                self.motor.write(PICKUP_BELT_DOWN, PICKUP_CONVEYOR_POWER)
                self.blocksCollected += 1
                print "LOWERING with", self.blocksCollected, "blocks inside"

        elif self.state == PICKUP_LOWERING:
            #print "Pickup limswitch", self.limSwitch.val
            if self.limSwitch.val:
                self.motor.write(0,0)
                if self.blocksCollected >= PICKUP_MAX_BLOCKS:
                    print "Going from PICKUP to DROPOFF"
                    self.blocksCollected = 0
                    return MODULE_DROPOFF
                else:
                    print "Going from PICKUP to FOLLOW"
                    return MODULE_FOLLOW

        else:
            print "Unexpected action index in PICKUP"
            self.blocksCollected = 0
            return MODULE_DROPOFF

        return MODULE_PICKUP