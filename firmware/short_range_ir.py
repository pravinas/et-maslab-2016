# short_range_ir
#
# Given an IR Reading, transform it into something more useful.
# This software is specifically built for Sharp Microelectronics GP2Y0A41SK0F.

from ..tamproxy.device import AnalogInput

class IR(AnalogInput):

    ## Please see the tamproxy AnalogInput class for more details.
    def __init__(self, tamproxy, pin):
        super(IR, self).__init__(tamproxy, pin)
        while self.id is None: pass
        self.start_continuous()

    ## Read the distance from the IR sensors in centimeters.
    # 
    # @return The distance in cm to an object.
    def read_ir(self):
        raw_data = self.val

        raise NotImplementedError
