from nltk.corpus import wordnet


while True :
    a = input("Enter a word: ")
    if a == 'q':
        break
    else:
        synset = wordnet.synsets(a)
        antonyms = []
        for syn in synset:
            print('definition: ', syn.definition())
            print('example: ', str(syn.examples()))
            print('synonym: ', syn.lemmas()[0].name())
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
            print('antonyms: '+ antonyms.__str__() )
            print('\n')

    print('Enter "q" to exit')


