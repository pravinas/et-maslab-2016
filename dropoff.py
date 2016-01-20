## dropoff.py
#
# Implements the DROPOFF module of the competition code.

class DropoffModule():
    def __init__(self, timer, servo):
        self.timeout = 7000
        self.waitTime = 500     # Time in ms to wait for the door to actually open.
        self.timer = timer
        self.servo = servo

    ## Return True if there was an error in initialization, False otherwise.
    def checkForInitializationErrors(self):
        # TODO: Make sure servo is initialized in the "closed" position.
        return False

    ## Set up the beginning of the dropoff process.
    def start(self):
        self.timer.reset()
        # TODO: Set the servo to open.

    ## Open the back door and drive "forwards," avoiding what needs to be avoided.
    #
    # @return   The value of the next module to return to.
    def run(self):

        # Allow timeout.
        if self.timer.millis() > self.timout:
            print "Timed out from DROPOFF to FIND"
            return MODULE_FIND

        if self.timer.millis() > self.waitTime:
            # TODO: Drive forwards after opening the door.
            raise NotImplementedError
        
        return MODULE_DROPOFF