import pandas as pd
import dotenv
from pdfminer.high_level import extract_text
import os
from pathlib import Path
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/upload/pdf")
def text_scraper(pdf):
    global text
    text = extract_text(pdf)

    return text

df = pd.read_csv('judges_appointed.csv')


text_scraper('upload_file.py')


from spacy.matcher import Matcher
from pdfminer.high_level import extract_text
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span 
# initialize the matcher
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher 

pattern = [{"ENT_TYPE": "PERSON"}, {"ENT_TYPE": "PERSON"}]
matcher.add("judge name", None, pattern) # 2nd argument is an optional callback


# call the matcher on the doc 
matches = matcher(doc)
#checking if matches is empty
if matches == []:
    pattern = [{"ENT_TYPE": "PERSON"}, {"ENT_TYPE": "PERSON"}, {"ORTH": ","}, {"ENT_TYPE": "PERSON"} ]
    matcher.add("judge name", None, pattern) # 2nd argument is an optional callback 
    matches = matcher(doc)

names_list = []

for _, start, end in matches:
    matched_span = doc[start:end]
    names_list.append(matched_span.text)

for x in range(len(names_list)):
    if df['name'].str.contains(names_list[x]).any():
        global judge
        judge = x
    else:
        "Judge not found."



print(names_list[judge])
        