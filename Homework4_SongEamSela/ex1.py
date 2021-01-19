import nltk

text="""A frequency distribution records the number of times each outcome of an experiment has occurred. For example, 
a frequency distribution could be used to record the frequency of each word type in a document. Formally, a frequency 
distribution can be defined as a function mapping from each sample to the number of times that sample occurred as an 
outcome. Frequency distributions are generally constructed by running a number of experiments, and incrementing the 
count for a sample every time it is an outcome of an experiment. """

grammar="""E: {<VB|VBD|VBG|VBP|VBN|VBZ><NNP|NNS>}
            {<DT>?<JJ>*<NN>}
            {<NN|JJ|VB|IN><NN|VB|IN>}
"""
reg=nltk.RegexpParser(grammar)
sentences=nltk.sent_tokenize(text)
for sentence in sentences:
    tokens= nltk.word_tokenize(sentence)
    tags=nltk.pos_tag(tokens)
    result=reg.parse(tags)
    print(result)