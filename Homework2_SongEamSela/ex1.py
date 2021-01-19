import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

while True:
    text = str(input("Enter a sentence: "))
    if text == "exit":
        break
    else:
        print("----------------------------------")
        # a. word tokenization
        words = nltk.word_tokenize(text)
        print(words)
        print("----------------------------------")
        # b. stopword removal
        stopWord = set(stopwords.words('english'))
        words_token = word_tokenize(text)
        result = [w for w in words_token if w not in stopWord]
        print(result)
        print("----------------------------------")
        # c. word stemming
        ps = PorterStemmer()
        for w in words_token:
            print(w, " : ", ps.stem(w))
        print("----------------------------------")
        # d. word lemmanization
        lm = WordNetLemmatizer()
        for w in words_token:
            print(w, " : ", lm.lemmatize(w))
        print("----------------------------------")




