## off.py
#
# Waits for the competition to actually start.

from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class OffModule(Module):

    def __init__(self, timer, switch):
        self.onSwitch   = switch    # DigitalInput
        self.timer      = timer     # Timer
        self.lastTime   = 0

    ## Nothing to set up
    def start(self):
        pass

    ## Wait for the switch to be turned on.
    #
    # @return   The value of the next module to return to.
    def run(self):
        if self.timer.millis() - self.lastTime > 100:
            self.lastTime = self.timer.millis()

            # Check button
            if self.onSwitch.val:
                return MODULE_FOLLOW
        return MODULE_OFF
