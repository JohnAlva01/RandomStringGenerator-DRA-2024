import itertools
import time
import sys
import os

class RandStrGenerator:
    # generate list of ascii integers for lower case alphabet letters
    low_case_ascii = list(range(97,123))
    max_char_ascii = max(low_case_ascii)
    min_char_ascii = min(low_case_ascii)
    num_char = max_char_ascii-min_char_ascii+1
    
    

    def __init__(self, length = 3):
        self.length = length
        self.randStrings = []

    def generateStrings(self):
        os.system('clear')
        print("Generating Strings...\n")

        a_str = list(itertools.repeat(self.low_case_ascii[0], self.length)) # ex. [97, 97, 97]
        max_size = self.max_char_ascii*self.length
        while (sum(a_str) < max_size) :
            self.randStrings.append("".join([chr(x) for x in a_str]))
            self.increment(len(a_str)-1, a_str)
        self.randStrings.append("".join([chr(x) for x in a_str]))
        
    def increment(self, index, alist):
        if (index < 0):
            return
        
        if alist[index] < self.max_char_ascii:
            alist[index] += 1
        else:
            alist[index] = self.min_char_ascii
            self.increment(index-1, alist)
                
    def printRandStrings(self):
        print(self.randStrings)
    
    def calcTotalStorage(self):
        if len(self.randStrings) == 0:
            print("There are no generated strings in the array")
        else:
            os.system('clear')

            match = len(self.randStrings) == self.num_char**self.length

            totalBytes = int(sys.getsizeof(self.randStrings[0]))*(self.num_char**self.length)
            totalMb = totalBytes / (10**6)
            print("Characters used: " + str(self.num_char) + "\n")
            print("Total Strings: " + str(len(self.randStrings)))
            print("Expected Strings: " + str(self.num_char**self.length))
            print("Total == Expected: " + str(match) + "\n")
            print("Total Storage: "+str(totalBytes)+" bytes")
            print("Total Storage: "+str(totalMb)+" MB\n")
    
    def findString(self, astring):
        try:
            index = self.randStrings.index(astring)
            print("Word found at index: "+str(index))
        except:
            print("Word not found")




    

if __name__ == "__main__":
    str_len = 6

    targetStr = "hello"

    r = RandStrGenerator(str_len)

    r.generateStrings()
    # r.printRandStrings()
    r.calcTotalStorage()
    #r.findString(targetStr)

    #print(r.randStrings[3276872])