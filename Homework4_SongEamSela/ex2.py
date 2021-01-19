from nltk.corpus import wordnet

a=input("Enter a word: ")
synset=wordnet.synsets(a)

for syn in synset:
    print('definition: ', syn.definition())
    print('example: ', str(syn.examples()))
    print('synonym: ', syn.lemmas()[0].name())
    print('\n')