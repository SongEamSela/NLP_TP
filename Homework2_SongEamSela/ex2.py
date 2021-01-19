import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize

text = open('data.txt','r').read().splitlines()
list_word = []

# a. sentence tokenization
file1 = open('sentence_token.txt', 'a')
for sen in text:
    words = sent_tokenize(sen)
    for i in words:
        file1.writelines(i+'\n')
file1.close()
print("----------------------------------")

# b. word tokenization
file2 = open('word_token.txt', 'a')
for sen in text:
    words = nltk.word_tokenize(sen)
    for i in words:
        file2.writelines(i+'\n')
file2.close()
print("----------------------------------")

# c. word lemmanization
file3 = open('lemmanization.txt', 'a')
lm = WordNetLemmatizer()
for sen in text:
    words = nltk.word_tokenize(sen)
    for w in words:
        file3.writelines(w+": "+lm.lemmatize(w)+"\n")
file3.close()
print("----------------------------------")

# d. stopword removal
file4 = open('stopWordRemoved.txt', 'a')
stopWord = set(stopwords.words('english'))
for sen in text:
    words_token = word_tokenize(sen)
    result = [w for w in words_token if w not in stopWord]
    for w in result:
        file4.writelines(w+'\n')
file4.close()
print("----------------------------------")
