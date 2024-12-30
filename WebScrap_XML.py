# Web scrapping for xml sheet (Get clean-readable data from xml file)

import os
os.chdir(r"D:\Data Analytics\Dec 28\xml_single articles\xml_single articles")

import xml.etree.ElementTree as ET

tree = ET.parse("769952.xml") 
root = tree.getroot()

root=ET.tostring(root, encoding='utf8').decode('utf8')

root 

import re, string, unicodedata    # Here 're' is regular expression
#import nltk

from bs4 import BeautifulSoup
#from nltk import word_tokenize, sent_tokenize
#from nltk.corpus import stopwords
#from nltk.stem import LancasterStemmer, WordNetLemmatizer

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text=re.sub('  ','',text)
    return text

sample = denoise_text(root)  # Clean data will be stored in sample
# print(sample)


# https://www.kaggle.com/code/mpwolke/scrapping-deutsche-wikibooks
#https://www.kaggle.com/code/zackakil/web-scraping-nlp-practical-exercise
