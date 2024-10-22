from wonderwords import RandomSentence

s = RandomSentence()

num = int(input("Enter number of sentences: "))

for i in range(num):
    print(s.sentence())
