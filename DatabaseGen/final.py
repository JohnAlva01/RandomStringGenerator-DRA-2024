from generatorClass.RandCharGen import RandCharGen
from generatorClass.RandSentGen import RandSentGen
from generatorClass.RandWordGen import RandWordGen
from generatorClass.SpecSentGen import SpecSentGen
import os
import random

def main():

    rcg = RandCharGen()
    rsg = RandSentGen()
    rwg = RandWordGen()
    folder_path = r"DatabaseGen/SpecTxtFiles"
    ssg = SpecSentGen(folder_path)

    randGenerators = [rcg, rsg, rwg, ssg]

    strLen = ssg.retMaxChar()
    numLines = 2000

    fileDest = r"DatabaseGen/finalTestTxtFiles"
    file_path = os.path.join(fileDest, f"database.txt")

    
    with open(file_path, 'w', encoding="utf-8") as fp:

        for i in range(numLines):
                aString = ""
                gen = random.choice(randGenerators)
                while len(aString) < strLen:
                    aString += gen.ret()
                    if (gen == rwg) or (gen == ssg):
                         aString += " "
                aString = aString[:strLen+1]
                aString += "\n"

                fp.write(aString)    

    fp.close()

main()