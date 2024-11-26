import nltk
import random
import string
import os
import time
import csv

from nltk.corpus import words
nltk.download('words')

# from nltk.corpus import wordnet
#n ltk.download('wordnet2022')

# importing list of english words & punctuation 
word_list = list(words.words())
wordListLen = len(word_list)
print(wordListLen)
puncList = list(string.punctuation)


#numWords = [10**2 , 10**3 , 10**4 , 10**5 , 10**6 , 10**7 , 10**8 ]
numWords = [10**2 , 10**3 , 10**4]

"""
numWords = []
for i in range(10**6+1):
    if (i % 10000) == 0:
        numWords.append(i)
"""
senLen = 10

includePunctuation = True

# path directory to read / write txt file to
dir = r'RandomTextGenerator\textFiles'

with open('wordData.csv','w', newline='') as sheets:

    writer = csv.writer(sheets)
    writer.writerow(["Num of Words","Time Taken (s)","Storage Used (MB)"])

    for c in numWords:
        row = []

        row.append(str(c))

        start = time.time()

        fileName = f'v1_{c}.txt'
        file_path = os.path.join(dir, fileName)

        with open(file_path, 'w') as fp:

            # algorithim to write to file based on parameters
            for i in range(round(c/senLen)):
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
            execTime = round((end-start) * 10**3 / 1000, 3)
            row.append(execTime)

            file_size = round(os.path.getsize(dir + "\\" + fileName) / (1024**2),3)
            row.append(file_size)

            print("\n"+f"Size: {file_size} MB")
            #file_size = round(os.path.getsize(dir + "\\" + fileName))
            #print(f"Size: {file_size} bytes")

            print(f"Time: {execTime} sec")
            print(f"Num of Words: {c}")
            
        fp.close()

        writer.writerow(row)

sheets.close()


    

