from generatorClass.RandCharGen import RandCharGen
from generatorClass.RandSentGen import RandSentGen
from generatorClass.RandWordGen import RandWordGen
from generatorClass.SpecSentGen import SpecSentGen
import os
import random

def main():
    folder_path = r"DatabaseGen/SpecTxtFiles"

    rcg = RandCharGen()
    rsg = RandSentGen()
    rwg = RandWordGen()
    ssg = SpecSentGen(folder_path)

    randGenerators = [rcg, rsg, rwg, ssg]
    
    fileDest = r"DatabaseGen/finalTestTxtFiles"
    file_path = os.path.join(fileDest, f"test.txt")

    tokens = 10
    numLines = 200

    with open(file_path, 'w') as fp:
        for i in range(numLines):
            
            aString = ""

            for j in range(tokens):

                # aString += random.choice(randGenerators).ret() + " "

                randInt = random.random()
                print(randInt)

                if 0 <= randInt < 0.4:
                    aString += rcg.ret()
                elif 0.4 <= randInt < 0.8:
                    aString += rwg.ret()
                elif 0.8 <= randInt < 0.9:
                    aString += rsg.ret()
                elif 0.9 <= randInt < 1:
                    aString += ssg.ret()
                
                aString += " "

            aString += "\n"

            fp.write(aString)

    fp.close()

main()