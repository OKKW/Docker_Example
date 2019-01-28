# app.py - a minimal flask api using flask_restful
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
import numpy as np
import pickle
from stop_words import get_stop_words
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import json
import os

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('query')

class HelloWorld(Resource):
    def get(self):

        args = parser.parse_args()
        input_X = args['query']
    
        stop_words = get_stop_words('en')
        loaded_bow_transformer = pickle.load(open('bow_transformer_py2.pkl', 'rb'))

        input_X2 = loaded_bow_transformer.transform([input_X])
        loaded_model = pickle.load(open('textmodel_py2.pkl', 'rb'))
        output ={'prediction':pd.Series(loaded_model.predict(input_X2)).to_json(orient='values')}

        return output
    

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
