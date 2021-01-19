import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

text = open('Test.txt','r').read()
stopWord = set(stopwords.words('english'))

sentences = sent_tokenize(text)
words = nltk.word_tokenize(text)
no_stopword = [w for w in words if w not in stopWord]

file1 = open('Terms_withStopwords.txt','a')
for w in words:
    file1.writelines(w+'\n')
file1.close()

file2 = open('Terms_withoutStopwords.txt','a')
for w in no_stopword:
    file2.writelines(w+'\n')
file2.close()


print('Number of sentence is ',len(sentences))
print('Number of all words is',len(words))
print('Number of all words exclude stopword is',len(no_stopword))

