from nltk.corpus import wordnet as wn

file = open("text.txt",'a')
antonyms = []
for s in list(wn.all_synsets('n')):
    file.write("word: " + s.name() + "\n")
    file.write('definition: ' + s.definition() + "\n")
    file.write('example: ' + s.examples().__str__() + "\n")
    for l in s.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
    file.write("antonyms: " + antonyms.__str__() + "\n")
    file.write("synonyms: " + s.lemma_names().__str__() + "\n")