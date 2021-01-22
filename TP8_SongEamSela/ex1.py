from textblob import TextBlob

# Preparing an input sentence
sentence = open('text.txt', 'r').read()

analysisPol = TextBlob(sentence).polarity
analysisSub = TextBlob(sentence).subjectivity

print(analysisPol)
print(analysisSub)