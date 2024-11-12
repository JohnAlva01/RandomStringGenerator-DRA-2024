import random
import os
import time

dir = r'RandomTextGenerator\textFiles'
fileName = f'v3.txt'
file_path = os.path.join(dir, fileName)

numSen = 10000
senLen = 50

numChar = numSen*senLen

start = time.time()
with open(file_path, 'w') as fp:
    for i in range(numSen):
        aStr = ""
        for k in range(senLen):
            aChar = random.randint(32,126)
            aStr += chr(aChar)
        aStr += "\n"
        fp.write(aStr)
end = time.time()
execTime = round((end-start) * 10**3 / 1000, 3)

fp.close()

file_size = round(os.path.getsize(dir + "\\" + fileName) / (1024**2),3)
print("\n"+f"Size: {file_size} MB")
print(f"Number of Char: {numChar}")
print(f"Time: {execTime} sec")

numLen = []

for i in range(10**7):
    if (i % 10000) == 0:
        numLen.append(i)

print(numLen)
