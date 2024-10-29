import nltk
import random
import string
import os
import time

nltk.download('words')
from nltk.corpus import words

# importing list of english words & punctuation 
word_list = words.words()
wordListLen = len(word_list)
print(wordListLen)

puncList = list(string.punctuation)

# creating parameters of text file
numSentences = 1000000
senLen = 10
numWords = numSentences * senLen

includePunctuation = True

# path directory to read / write txt file to
dir = r'RandomTextGenerator\textFiles'
fileName = 'example.txt'
file_path = os.path.join(dir, fileName)

# start timer
start = time.time()

# write to file
with open(file_path, 'w') as fp:

    # algorithim to write to file based on parameters
    for i in range(numSentences):
        sentence = ""
        for k in range(senLen):
            wordIndex = round(random.random() * wordListLen)-1
            puncRand = random.random()
            
            if (k != (senLen-1)):
                #print(wordIndex)
                try:
                    sentence += word_list[wordIndex] + " "
                except IndexError:
                    print("List index = " + str(wordIndex))

                if (puncRand >= 0.8):
                    sentence += random.choice(puncList) + " "
            else:
                sentence += word_list[wordIndex] + "\n"
        fp.write(sentence)

end = time.time()
fp.close()

execTime = round((end-start) * 10**3 / 1000, 3)


file_size = round(os.path.getsize(dir + "\\" + fileName) / (1024**2),3)
print("\n"+f"Size: {file_size} MB")
#file_size = round(os.path.getsize(dir + "\\" + fileName))
#print(f"Size: {file_size} bytes")

print(f"Time: {execTime} sec")
print(f"Num of Words: {numWords}")



    

