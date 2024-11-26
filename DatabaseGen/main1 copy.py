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

    with open(file_path, 'w') as fp:


    fp.close()

main()