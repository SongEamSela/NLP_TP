from nltk.corpus import stopwords

stopWord = set(stopwords.words('english'))
file = open('StopWord.txt','a')
file.write(str(len(stopWord))+'\n')
for w in stopWord:
    file.writelines(w+'\n')
file.close()