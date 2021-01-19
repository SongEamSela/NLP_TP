import nltk
from nltk.stem import WordNetLemmatizer

text = open('test_text.txt','r').read()
sentences = nltk.sent_tokenize(text)
nouns=[]
verbs=[]
adjectives=[]

lemmatizer=WordNetLemmatizer()
for sentence in sentences:
    tokens=nltk.word_tokenize(sentence)
    tags=nltk.pos_tag(tokens)
    for word,pos in tags:
        if pos in ['NN','NNS','NNP','NNPS']:
            nouns.append(lemmatizer.lemmatize(word))
        elif pos in ['VB','VBD','VBG','VBN','VBP','VBZ']:
            verbs.append(lemmatizer.lemmatize(word,pos='v'))
        elif pos in ['JJ','JJR','JJS']:
            adjectives.append(lemmatizer.lemmatize(word,pos='a'))

file = open('output_text_BaseForm.txt','a')

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