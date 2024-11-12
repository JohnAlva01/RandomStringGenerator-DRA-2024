import random
import os
import time

class RandCharGen:

    def __init__(self):
        self.charSet = list(range(32,127))

    def ret(self):
        return chr(random.choice(self.charSet))