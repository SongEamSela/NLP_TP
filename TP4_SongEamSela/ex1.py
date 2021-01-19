import nltk

text = open('data.txt','r').read()
file = open('compound-noun.txt','a')

grammar="""P:{<NN><NN>}"""
re=nltk.RegexpParser(grammar)
sentences=nltk.sent_tokenize(text)
for sentence in sentences:
    tokens=nltk.word_tokenize(sentence)
    tags=nltk.pos_tag(tokens)
    result=re.parse(tags)
    for subTree in result:
        if isinstance(subTree,nltk.tree.Tree):
            if subTree.label()=='P':
                file.write(subTree.__str__()+'\n')