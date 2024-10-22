from essential_generators import DocumentGenerator

testDg1 = True
testDg2 = True

dg1 = DocumentGenerator()
dg2 = DocumentGenerator()

dg2.init_sentence_cache(5000)

numSentences = 30

if testDg1:     
    for i in range(0,numSentences):
        print(f'{i}. {dg1.sentence()}')


if testDg2:    
    for i in range(0,numSentences):
        print(f'{i}. {dg2.sentence()}')