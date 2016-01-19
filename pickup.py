## pickup.py
#
# Implements the PICKUP module of the competition code.

class PickupModule():
    def __init__(self, timer, conveyorMotor, conveyorEncoder, conveyorPower, conveyorEncoderLimit):
        self.timer = timer
        self.conveyorMotor = conveyorMotor
        self.conveyorEncoder = conveyorEncoder
        self.conveyorPower = conveyorPower
        self.conveyorEncoderLimit = conveyorEncoderLimit
        self.blocksPickedUp = 0
    
    ## Set up the beginning of the pickup process.
    def startPickupModule(self):
        self.conveyorEncoder.write(0)
        self.conveyorMotor.write(True, self.conveyorPower)
        self.moduleTimer.reset()

    ## Pick up a block from the block capture mechanism.
    #
    # Move the conveyor belt upwards until the encoders indicate that
    # the block has moved far enough. Then move the conveyor belt back.
    #
    # @return   The value of the next module to return to.
    def runPickupModule(self):

        # Allow timeout.
        if self.moduleTimer.millis() > self.module["timeout"]:
            print "Timed out from PICKUP to FIND"
            return MODULE_FIND

        encval = self.conveyorEncoder.val

        # Move up the conveyor belt until it hits the encoder limit.
        if encval > self.conveyorEncoderLimit:
            self.conveyorMotor.write(True, self.conveyorPower)
        else:
            self.conveyorMotor.write(False), self.conveyorPower

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
