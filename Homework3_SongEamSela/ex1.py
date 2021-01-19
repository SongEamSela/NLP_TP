import nltk

text = """In some respects, the rise of Python is as surreal and surprising as the British comedy group it was named 
after, and in its own niche the coding language has become just as famous and influential. 

The programming language was started as a side project by Dutch programmer Guido van Rossum. In the late 1980s, 
van Rossum was working on a distributed system at the Centrum Wiskunde & Informatica (CWI), the Dutch national 
research center for math and computer science. Frustrated by the inadequacies of existing programming languages, 
he decided to create a new one — one that would be both easy-to-use and capable. """

sentences=nltk.sent_tokenize(text)
nouns=[]
adjectives=[]
verbs=[]
for sen in sentences:
    tokens=nltk.word_tokenize(sen)
    tags=nltk.pos_tag(tokens)
    for word,pos in tags:
        if pos in ['NN','NNS']:
            nouns.append(word)
        elif pos in ['JJ']:
            adjectives.append(word)
        elif pos in ['VB','VBN','VBZ','VBG','VBP']:
            verbs.append(word)
print('Nouns: ',nouns)
print('Adjectives: ',adjectives)
print('Verbs: ',verbs)