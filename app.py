from datetime import datetime
import flask
from flask import Flask, render_template
from flask import request

from nlpsection.queryexecutor import execute_query,genarate_query
from nlpsection.util import create_response

# from
import json
import base64



app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route('/')
@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/executeQuery', methods=['GET', 'POST'])
def upload():

    strLine = request.json['InputText']

    # decodedval = base64.b64decode(requestObject['data'])
    print('Input Natural query : ', strLine)
    result = execute_query(strLine)

    processed_result = create_response(result)


    return processed_result

@app.route('/generateQuery', methods=['POST'])
def res_massage():
    strLine = request.json['InputText']

    # decodedval = base64.b64decode(requestObject['data'])
    print('Input Natural query : ', strLine)
    result = genarate_query(strLine)


    return "The Corrected Sentence"



if __name__ == '__main__':
    app.run(port=5000, debug=True)