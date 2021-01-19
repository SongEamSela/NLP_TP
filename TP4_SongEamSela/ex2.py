import nltk
text = open('data.txt', 'r').read()
grammar="""E:{<VB|VBD|VBG|VBP|VBN|VBZ><NN|NNP|NNS>}
{<JJ><NN>}"""
re=nltk.RegexpParser(grammar)
sentences=nltk.sent_tokenize(text)
for sentence in sentences:
    tokens=nltk.word_tokenize(sentence)
    tags=nltk.pos_tag(tokens)
    result=re.parse(tags)
    for subtree in result:
        if isinstance(subtree,nltk.tree.Tree):
            if subtree.label()=='E':
                print(subtree.__str__())