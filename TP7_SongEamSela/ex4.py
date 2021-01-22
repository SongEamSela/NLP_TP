from bs4 import BeautifulSoup
import re
import requests
from spacy import displacy
import spacy

nlp = spacy.load('en_core_web_sm')


def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + str(ent.start_char) + ' - ' + str(ent.end_char)
                  + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
        else:
            print('No named entities found.')


doc1 = url_to_string("https://www.w3schools.com/sql/")

# a.
show_ents(nlp(doc1))

# b.

displacy.render(nlp(doc1), style='ent', jupyter=True)
