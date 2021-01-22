from textblob import TextBlob

text = str(input("Enter text: "))
blob = TextBlob(text)
orgLang = blob.detect_language()
print("en = English, fr = France, th = Thai, zh = Chinese, ko = Korean")
desLang = str(input("Enter your destination language: "))


print(blob.translate(to=desLang))