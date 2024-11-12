import glob
import random

class SpecSentGen:

    def __init__(self, folderPath):
        self.specSen = []
        for file in glob.glob(folderPath + "/*.txt"):
            with open(file, 'r') as f:
                for line in f:
                    self.specSen.append(line.strip())
    
    def ret(self):
        return random.choice(self.specSen)


