from generatorClass.RandCharGen import RandCharGen
from generatorClass.RandSentGen import RandSentGen
from generatorClass.RandWordGen import RandWordGen
from generatorClass.SpecSentGen import SpecSentGen
import os
import random

print("Working directory:", os.getcwd())
print("Files:", os.listdir("."))

def main():
    folder_path = os.getcwd() + r"\SpecTxtFiles"
    print(folder_path)

    rcg = RandCharGen()
    rsg = RandSentGen()
    rwg = RandWordGen()
    ssg = SpecSentGen(folder_path)

    randGenerators = [rcg, rsg, rwg, ssg]
    
    fileDest = os.getcwd() + r"\finalTestTxtFiles"
    print(fileDest)

    strLen = 100
    numLines = 200
    
    for gen in randGenerators:

        file_path = os.path.join(fileDest, f"{gen.__class__.__name__}.txt")

        with open(file_path, 'w', encoding="utf-8") as fp:
            for i in range(numLines):
                
                aString = ""

                while len(aString) < strLen:
                    aString += gen.ret().strip() + " "


                aString = aString[:strLen+1]
                aString += "\n"

                fp.write(aString)

        fp.close()

main()