# app.py - a minimal flask api using flask_restful
from flask import Flask, jsonify, request, render_template, make_response
from flask_restful import Resource, Api,reqparse
import json

app = Flask(__name__)
#api = Api(app)

@app.route('/nlp', methods=['POST'])
def nlp():
    #json_data = request.get_json(force=True)
    #res = ast.literal_eval(request.data.decode)
    #res['mujani'].append('francis')
    name = "hello simplon"
    return name

        #return {"result":result}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')