import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

text = open('Test.txt','r').read()
stopWord = set(stopwords.words('english'))

words = nltk.word_tokenize(text)
no_stopword = [w for w in words if w not in stopWord]

file3 = open('text-preporcessing.txt', 'a')
lm = WordNetLemmatizer()
no_stopword.sort()
for w in no_stopword:
    file3.writelines(lm.lemmatize(w)+"\n")
file3.close()