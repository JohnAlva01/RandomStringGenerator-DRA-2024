
from essential_generators import DocumentGenerator

class RandSentGen:

    def __init__(self):
        self.documentGen = DocumentGenerator()
    
    def ret(self):
        astr = self.documentGen.sentence()
        cleaned_astr = astr.replace('\n', "").strip()
        return cleaned_astr