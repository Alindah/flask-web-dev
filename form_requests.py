"""
This app returns the length of a given string.

>>> curl http://127.0.0.1:5000/ -d "data=four" -X GET
>>> curl http://127.0.0.1:5000/
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

# https://pythonise.com/series/learning-flask/rendering-html-files-with-flask
@app.route('/')
def index():
	return render_template("index.html")

# https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
@app.route('/', methods = ['POST'])
def handle_data():
    data = request.form["test_input"]
    return str(len(data))

api.add_resource(ReturnLength, '/')

if __name__ == '__main__':
    app.run(debug=True)

