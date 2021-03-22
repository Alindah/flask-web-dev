"""
This app returns the length of a given string.

>>> curl http://127.0.0.1:5000/ -d "data=four" -X GET
- Output should be { 4 }

"""
from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ReturnLength(Resource):
    def get(self):
    	data = request.form['data']
    	return len(data)

api.add_resource(ReturnLength, '/')

if __name__ == '__main__':
    app.run(debug=True)

