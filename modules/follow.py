# follow.py

from module import Module
from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import *

class FollowModule(Module):
    
    def __init__(self, timer):
        self.timer = timer
        # TODO: Once Gilbert finishes his part of the wall follower
    