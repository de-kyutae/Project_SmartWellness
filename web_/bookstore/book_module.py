import base64

import requests
from bson import ObjectId
from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
import random

app = Flask(__name__)
filename = 'atlas_connection_info.txt'


# MongoDB에 연결
class MyMongoClient(object):
    def __init__(self):
        with open(filename, encoding='utf-8') as f:
            self.atlas_connection_info = f.read()
        self.client = MongoClient(self.atlas_connection_info)
        self.database = self.client["kim_db"]
        self.collection = self.database["books"]

#@app.route('/weather', methods=['GET'])


# MongoDB atlas에 접속
@app.route('/atlas_connection_info')
def atlas_connection_info():
    with open(filename, encoding='utf-8') as f:
        atlas_info = f.read()
    return render_template('atlas_connection_info.html', atlas_info=atlas_info)


@app.route('/atlas_connection_info_update', methods=['POST'])
def atlas_connection_info_update():
    atlas_info_update = request.form['atlas_connect_info']
    with open('atlas_connection_info.txt', 'w', encoding='utf-8') as f:
        f.write(atlas_info_update)
    return render_template('atlas_connection_info_update.html', atlas_info_update=atlas_info_update)


# 첫 화면
@app.route('/')
def home():
    city = 'daegu'
    appid = 'e5d4ba22d1c0aae4130753ea87c69eec'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'
    res = requests.get(url)
    # weather_data = json.loads(res.text)
    weather_data = res.json()

    description = weather_data["weather"][0]["description"]
    icon = weather_data["weather"][0]["icon"]
    temp = weather_data["main"]["temp"] - 273
    temp = round(temp, 1)
    return render_template('index.html', description=description,
                           icon=icon, temp=temp
                           )


@app.route('/book_add', methods=['GET'])
def book_add():
    return render_template('book_add.html')


@app.route('/book_add_process', methods=['POST'])
def book_add_process():
    # client = MongoClient("mongodb://localhost:27017/")
    # database = client["song-db"]
    # collection = database["books"]
    myclient = MyMongoClient()
    title = request.form['title']
    file = request.files['file']
    author = request.form['author']
    price = request.form['price']
    isbn = request.form['isbn']
    encoded_data = base64.b64encode(file.read())

    doc = {'title': title, 'encoded_data': encoded_data, 'author': author,
           'price': price, 'isbn': isbn, 'created_date': datetime.now()}

    # flash('Thanks for registring')
    # result = collection.insert_one(doc)
    result = myclient.collection.insert_one(doc)

    book_add_result = None
    if result.inserted_id is not None:
        print(result.inserted_id)
        book_add_result = "정상 등록"
    else:
        book_add_result = "등록 실패"

    return render_template('book_add_result.html',
                           book_add_result=book_add_result)


@app.route('/book_search', methods=['GET'])
def book_search():
    return render_template('book_search.html')


@app.route('/book_search_result', methods=['POST'])
def book_search_result():
    item = request.form['item_to_search']
    data = request.form['data_to_search']

    myclient = MyMongoClient()
    if item == 'id':
        query = {'_id': data}
    elif item == 'title':
        query = {'title': data}
    books = myclient.collection.find(query)

    return render_template('book_search_result.html', books=books)


@app.route('/book_id_search', methods=['GET'])
def book_id_search():

    return render_template('book_id_search.html')


@app.route('/book_id_search_process', methods=['POST'])
def book_id_search_process():
    # client = MongoClient()
    # database = client["song-db"]
    # collection = database["books"]
    myclient = MyMongoClient()
    _id = request.form['id']

    doc = myclient.collection.find_one({'_id': ObjectId(_id)})
    title = doc['title']
    decoded_data = doc['encoded_data'].decode('utf-8')
    # decoded_data = base64.b64decode(encoded_data)

    img_src_data = f'data:image/png;base64, {decoded_data}'

    return render_template('book_id_search_result.html',
                           title=title, img_src_data=img_src_data)


@app.route('/book_list', methods=['GET'])
def book_list():
    # client = MongoClient()
    # database = client["kim_db"]
    # collection = database["books"]
    myclient = MyMongoClient()
    total_count = myclient.collection.find().count()
    print(total_count)

    books = myclient.collection.find()
    return render_template('book_list.html', books=books, total_count=total_count)


    # book_list = []
    # for encoded_data in books:
    #     decoded_data = books['encoded_data'].decode('utf-8')
    #     # decoded_data = base64.b64decode(encoded_data)
    #     img_src_data = f'data:image/png;base64, {decoded_data}'
    #     decoded_data['encoded_data'] = img_src_data
    #     book_list.append(decoded_data)
    # return render_template('book_list.html', book_list=book_list, total_count=total_count)



@app.route('/book_details/<_id>')
def book_details(_id=None):
    print(_id)
    return render_template('book_detail.html')


@app.route('/lotto_game')
def lotto_game():
    # my_lotto = []
    com_lotto = []
    # while len(my_lotto) is not 6:
    #     my_num = random.randint(1, 45)
    #     if my_num not in my_lotto:
    #         my_lotto.append(my_num)

    while len(com_lotto) is not 6:
        com_num = random.randint(1, 45)
        if com_num not in com_lotto:
            com_lotto.append(com_num)


if __name__ == '__main__':
    app.run()
