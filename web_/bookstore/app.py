from bson import ObjectId
from flask import Flask, render_template, request
import base64
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = '이미자'
    return render_template('index.html', name=name)


@app.route('/book_add', methods=['GET'])
def book_add():
    return render_template('book_add.html')


@app.route('/book_add_process', methods=['POST'])
def book_add_process():
    client = MongoClient("mongodb://localhost:27017/")
    database = client["kim_db"]
    collection = database["books"]

    title = request.form['title']
    file = request.files['file']
    author = request.form['author']
    price = request.form['price']
    isbn = request.form['isbn']
    encoded_date = base64.b64encode(file.read())

    doc = {'title': title, 'encoded_date': encoded_date, 'author': author,
           'price': price, 'create_date': datetime.now()}
    result = collection.insert_one(doc)

    book_add_result = None
    if result.inserted_id is not None:
        print(result.inserted_id)
        book_add_result="정상 등록"
    else:
        book_add_result="등록 실패"

    return render_template('book_add_result.html')

@app.route('/book_id_search', methods=['GET']) #검색하는 웹페이지 띄우기
def book_id_search():
    return render_template('book_id_search.html')


@app.route('/book_id_search_process', method=['POST'])
def book_id_search_process():
    client = MongoClient()
    database = client["kim_db"]
    collection = database["books"]
    _id = request.form['id']

    doc = collection.find_one({'_id': ObjectId(_id)})
    title = doc['title']
    encoded_data = doc['encoded_data'].decode('utf-8')
    img_src_data = f'data:image/png;base64, {encoded_data}'

    return render_template('book_id_search_result.html', title=title, img_src_data=img_src_data)


@app.route('/jiji', methods=['GET','POST'])
def jiji():
    if request.method == 'POST':
        year = request.form['year']
        jiji_list = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']
        jiji_index = (year - 4) % 12
        myjiji=jiji_list[jiji_index]
        return render_template('jiji.html', myjiji=myjiji)
    else:
        return render_template('jiji.html')


if __name__ == '__main__':
    app.run()
