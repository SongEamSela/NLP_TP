from textblob import TextBlob

text = open('text.txt','r').read()
blob = TextBlob(text)
org = blob.detect_language()

file1 = open('data.txt', 'w')
nounPh = blob.noun_phrases
file1.write(str(nounPh))

print("en = English, fr = France, th = Thai, zh = Chinese, ko = Korean")
desLang = str(input("Choose destination language: "))

file = open('destinationLanguage.txt', 'w')

for w in nounPh :
    blob1 = TextBlob(w)
    tran = blob1.translate(to=desLang)
    file.write(str(tran)+'\n')


