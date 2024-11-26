import nltk
import random
from nltk.corpus import words
nltk.download('words')

class RandWordGen:

    def __init__(self):
        self.wordList = list(words.words())

    def ret(self):
        return random.choice(self.wordList)