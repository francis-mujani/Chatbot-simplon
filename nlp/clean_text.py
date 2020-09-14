### First round of text cleaning technique 
import re
import string
import pandas as pd


def clean_text_(text):
    # mettrez tout les text en lowercase et remove text in square brackets aussi remove ponctuation
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\W*\d\W*', '', text)
    text = re.sub('\n', ' ', text)
    return text

round = lambda x: clean_text_(x)


data = pd.read_csv('data.csv')

# Nettoyage
data['Question'] = data.Question.apply(round)
data['Reponse'] = data.Reponse.apply(round)

data.to_csv('dataclean.csv', index=False)