from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
client = MongoClient(
    'mongodb+srv://' + os.getenv('MID') + ':' + os.getenv(
        'MPW') + '@cluster0.ahcokcb.mongodb.net/?retryWrites=true&w=majority')
db = client.Cluster0

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/api/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive,
    }
    db.users.insert_one(doc)
    return jsonify({'msg': '주문 완료!'})


@app.route("/api/mars", methods=["GET"])
def web_mars_get():
    return jsonify({'data': list(db.users.find({}, {'_id': False})), 'msg': '조회 성공!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
