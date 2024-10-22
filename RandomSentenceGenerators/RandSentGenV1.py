"""
from wonderwords import RandomSentence

s = RandomSentence()

num = int(input("Enter number of sentences: "))

for i in range(num):
    print(s.sentence())

"""

from wonderwords import RandomWord
w = RandomWord()
sentenceLen = 13
numSentences = 30
for i in range(numSentences):
    sen = []
    for j in range(sentenceLen):
        sen.append(w.word(include_categories=["adjective","noun","verb"]))
    print(" ".join(sen))
    
