import nltk

text = open('input.txt','r').read()
sentences = nltk.sent_tokenize(text)
nouns=[]
verbs=[]
adjectives=[]
adverb = []
# a. Extract individual words based on part-of-speech such as adverb, verb, and noun
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
        elif pos in ['RB','RBR','RBS']:
            adverb.append(word)

file = open('output.txt','w')

file.write('Nouns: ')
for noun in nouns:
    file.write(noun+', ')
file.write('\n')

file.write('Verb: ')
for verb in verbs:
    file.write(verb+', ')
file.write('\n')

file.write('Adjective: ')
for adjective in adjectives:
    file.write(adjective+', ')
file.write('\n')

file.write('Adverb: ')
for adv in adverb:
    file.write(adv + ' , ')
file.write('\n')

file.close()

# b. Extract relation terms for adjective-noun pair.

grammar="NP: {<DT>?<JJ>*<NN>}"
re=nltk.RegexpParser(grammar)
sentences=nltk.sent_tokenize(text)
for sentence in sentences:
    tokens=nltk.word_tokenize(sentence)
    tags=nltk.pos_tag(tokens)
    result=re.parse(tags)
    for subtree in result:
        if isinstance(subtree,nltk.tree.Tree):
            if subtree.label()=='NP':
                print(subtree.__str__())