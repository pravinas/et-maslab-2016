## dropoff.py
#
# Implements the DROPOFF module of the competition code.

class DropoffModule():
    def __init__(self, timer, servo):
        self.timeout = 7000
        self.timer = timer
        self.servo = servo

    ## Set up the beginning of the dropoff process.
    def start(self):
        self.timer.reset()
        # TODO: Set the servo to open.

    ## Open the back door and drive "forwards," avoiding what needs to be avoided.
    #
    # @param waitTime   Time in ms to wait for the door to actually open.
    # @return   The value of the next module to return to.
    def run(self, waitTime = 500):
        assert MODULE_DROPOFF == self.module

        # Allow timeout.
        if self.moduleTimer.millis() > self.module["timeout"]:
            print "Timed out from DROPOFF to FIND"
            self.startFindModule()
            return

        if self.moduleTimer.millis() > waitTime:
            # TODO: Drive forwards after opening the door.
