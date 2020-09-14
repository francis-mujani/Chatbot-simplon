from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
# import vertorizer
from model import Question
from model import vectorizer

# import clean text
from clean_text import clean_text_

# import data
data = pd.read_csv('data.csv')


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
# parser.add_argument('number', type=float, required=True)
parser.add_argument('input', type=str, required=True)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

class Square(Resource):
    def post(self):
        args = parser.parse_args()
        #number = args['number']
        # res = number * number
        input_ = args['input']
        input_ = clean_text_(input_)

        input_ = vectorizer.transform(np.array([input_]))
        input_ = input_.toarray()

        retour = np.argmax(cosine_similarity(input_, Question))
        retour = data['Reponse'].iloc[retour]
        print(retour)
        return {'square': retour}, 200


api.add_resource(HelloWorld, '/hello')
api.add_resource(Square, '/square')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

