import glob
import random

class SpecSentGen:

    def __init__(self, folderPath):
        self.specSen = []
        self.maxChar = 0
        for file in glob.glob(folderPath + "/*.txt"):
            with open(file, 'r') as f:
                for line in f:
                    aline = line.strip()
                    if len(aline) > self.maxChar:
                        self.maxChar = len(aline)
                    self.specSen.append(aline)

    
    def ret(self):
        a = ""
        if self.specSen:
            a = random.choice(self.specSen)
            self.specSen.remove(a)
        return a

    def hasItems(self):
        return len(self.specSen) != 0
    
    def retMaxChar(self):
        return self.maxChar

