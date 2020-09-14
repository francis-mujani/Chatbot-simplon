import requests
from bs4  import BeautifulSoup
import re
from nltk.corpus import stopwords
import pandas as pd
import nltk
import numpy as np
import random
import string 
from nltk.stem.snowball import SnowballStemmer
import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# scrap simplon
from header import head
url='https://simplon.co/anti-faq'
r=requests.get(url,headers=head)
print(url)
print(r.status_code)
soup = BeautifulSoup(r.content,"html")

# recupe FAQ
question = []
reponse = []
for elem in soup.findAll('h5',{'class':'mb-0 question'}):
    question.append(elem.text.strip())
    
for elem in soup.findAll('div',{'class':'card-body'}):
    reponse.append(elem.text.strip())

# create data
data = pd.DataFrame({'Question':question , 'Reponse':reponse})
data.to_csv('data.csv', index=False)
