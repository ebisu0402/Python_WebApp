from flask import Flask
from flask import Flask, request
from flask import Flask, request,render_template
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def inex():
    return "Response Data"


@app.route("/another")
def another():
    return "Another Response"


@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route('/exercise_request/<data>')
def test_request_param(data):
    return f'exercise_request:{data}'

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise', methods=['GET', 'POST'])
def exercise():
    if request.method == 'POST':
        my_name = request.form.get('my_name', '') 
        return f'Hello, {my_name}!'  
    return render_template('exercise.html')

@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)


