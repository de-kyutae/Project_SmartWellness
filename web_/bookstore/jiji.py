from bson import ObjectId
from flask import Flask, render_template, request
import base64
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def jiji():
    if request.method == 'POST':
        year = int(request.form['year'])
        jiji_list = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']
        jiji_index = (year - 4) % 12
        myjiji = jiji_list[jiji_index]
        return render_template('jiji.html', myjiji=myjiji)
    else:
        return render_template('jiji.html')


if __name__ == '__main__':
    app.run()