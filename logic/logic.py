## logic.py
#
# File for algorithms that turn sensor data into more useful information.


class Logic():
    def __init__(self):
        # TODO
        pass
        
    ## Given the camera data, outputs an angle at which the robot should move.
    #
    # @param block  The block data that is output from the camera.
    # @param stack  The stack data that is output from the camera.
    # @return   An angle corresponding to the block, if it exists, otherwise an 
    #           angle corresponding to the stack. If neither exists, return None.
    def findTargetFromCameraData(self, block, stack):
        # TODO: Perhaps assign to Lotta to calibrate? This needs to be calibrated
        #       from its position on the robot itself.
        return 0

    ## Given the current target angle, use sensor data to update.
    #
    # @param target The current target angle.
    # @param time   The number of milliseconds that have passed since last update.
    def bayesianTargetUpdate(self, target):
        # TODO: Definitely need more arguments. Need to think about how to implement.
        return target