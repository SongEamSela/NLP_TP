import nltk
import matplotlib
from nltk.corpus import stopwords

text = open('data.txt', 'r').read()
stopWord = set(stopwords.words('english'))

# a. Count number of each word(exclude stopwords)

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

wordlist = text.split()
no_stopword = removeStopwords(wordlist, stopWord)

freq_word = nltk.FreqDist(no_stopword)
print(freq_word)
filter_words = dict([(m, n) for m, n in freq_word.items()])

for key in sorted(filter_words):
    print("%s: %s" % (key, filter_words[key]))

# b. Plot a graph representing word frequency (exclude stopwords)

freq_word.plot(30,cumulative=False)