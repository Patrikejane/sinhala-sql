from datetime import datetime
import flask
from flask import Flask, render_template, make_response
from flask import request
from flask_cors import CORS
import re

# from nlpsection.queryexecutor import execute_query,generate_query
from nlpsection.QueryExecutor import QueryExecutor
from nlpsection.util import create_response

# from
import json
import base64

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


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
    strLine = request.json['query']

    # decodedval = base64.b64decode(requestObject['data'])
    print('Input Natural query : ', strLine)
    executer = QueryExecutor(strLine)
    result, columns, type = executer.execute_query()

    # processed_result = create_response(result)

    if(type[0] == 'calculation'):
        m = re.findall('\((.*?)\)', columns[0])[0]
        columns = (type[1] + ' ' + m,)

        key = list(result[0].keys())[0]
        value = result[0][key]

        calculation_result = {}

        calculation_result[type[1] + ' ' + m] = str(value)

        result = [calculation_result]

    json_data = {}
    json_data['status'] = "success"
    json_data['result'] = result
    json_data['columns'] = list(columns)
    json_data['message'] = ''
    resp = make_response(json.dumps(json_data), 200)
    resp.headers['Content-type'] = 'application/json; charset=utf-8'

    return resp


@app.route('/generateQuery', methods=['POST'])
def res_massage():
    print("started")
    strLine = request.json['input']

    # decodedval = base64.b64decode(requestObject['data'])
    print('Input Natural query : ', strLine)

    executer = QueryExecutor(strLine)
    result = executer.generate_query()

    json_data = {}
    json_data['status'] = "success"
    json_data['query'] = result
    json_data['message'] = ''
    resp = make_response(json.dumps(json_data), 200)
    resp.headers['Content-type'] = 'application/json; charset=utf-8'
    return resp


if __name__ == '__main__':
    app.run(port=5000, debug=True)
