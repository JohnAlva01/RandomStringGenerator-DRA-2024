
from essential_generators import DocumentGenerator

class RandSentGen:

    def __init__(self):
        self.documentGen = DocumentGenerator()
    
    def ret(self):
        return self.documentGen.sentence()