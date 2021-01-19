from nltk.corpus import wordnet

word = str(input("Please input a word : "))
word_sets = wordnet.synsets(word)
for set in word_sets:
    print('Definition: ',set.definition())
    print('Example: ', set.examples())