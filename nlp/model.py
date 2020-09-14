# TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

dataclean = pd.read_csv('dataclean.csv')
print('loading dataset...')
# create vectorizer 
vectorizer = TfidfVectorizer()

Question = vectorizer.fit_transform(dataclean['Question'])
print('Vectorizer Done !')
# print(vectorizer_quest.get_feature_names())

# je transforme la matrice en Array
Question = Question.toarray()
print(Question.shape)

#-------------------------------------------------------

