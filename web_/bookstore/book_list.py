from bson import ObjectId
from flask import Flask, render_template, request
import base64
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)


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

    book_add_result = ''
    if result.inserted_id is not None:
        print(result.inserted_id)
        book_add_result = "정상 등록"
    else:
        book_add_result = "등록 실패"

    return render_template('book_add_result.html', book_add_result=book_add_result)


@app.route('/book_id_search', methods=['GET'])
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


@app.route('/book_list', method=['GET'])
def book_list():
    client = MongoClient("mongodb://localhost:27017/")
    database = client["kim_db"]
    collection = database["books"]
    cursor = collection.find()

    title_list = []
    img_src_data_list = []
    author_list = []
    price_list = []
    isbn_list = []
    create_data_list = []

    for doc in cursor:
        title = doc['title']
        decoded_data = doc['encoded_data'].decode('utf-8')
        img_src_data = f'data:image/png;base64, {decoded_data}'
        author = doc['author']
        price = doc['price']
        isbn = doc['isbn']
        create_data = doc['create_data']

        title_list.append(title)
        img_src_data_list.append(img_src_data)
        author_list.append(author)
        price_list.append(price)
        isbn_list.append(isbn)
        create_data_list.append(create_data)

    return render_template('book_list.html', title_list=title_list, img_src_data_list=img_src_data_list,
                           author_list=author_list, price_list=price_list,
                           isbn_list=isbn_list, create_data_list=create_data_list)


if __name__ == '__main__':
    app.run()
