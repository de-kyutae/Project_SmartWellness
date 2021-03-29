from bson import ObjectId
from flask import Flask, render_template, request
import base64
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)


@app.route('/book_list', methods=['GET'])
def book_list():
    client = MongoClient()
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