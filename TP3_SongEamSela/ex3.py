import nltk
import numpy as np

text = open('Test.txt','r').read()
sentences = nltk.sent_tokenize(text)
nouns=[]
verbs=[]
adjectives=[]

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    for word, pos in tags:
        if pos in ['NN','NNS','NNP','NNPS']:
            nouns.append(word)
        elif pos in ['VB','VBD','VBG','VBN','VBP','VBZ']:
            verbs.append(word)
        elif pos in ['JJ','JJR','JJS']:
            adjectives.append(word)

file = open('ouput-extracted-terms.txt','a')

file.write('Nouns:')
for noun in nouns:
    file.write(noun+', ')
file.write('\n')

file.write('Verb:')
for verb in verbs:
    file.write(verb+', ')
file.write('\n')

file.write('Adjective:')
for adjective in adjectives:
    file.write(adjective+', ')
file.write('\n')

file.close()