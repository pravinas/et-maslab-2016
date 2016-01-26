# Check Module
# Checks to see what color the aquired block is, then spits out the block if it is the wrong color

from module import Module

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class CheckModule(Module):

	def __init__ (self, timer, leftMotor, rightMotor, color):
		self.