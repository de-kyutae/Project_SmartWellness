from bson import ObjectId
from flask import Flask, render_template, request
import base64
from pymongo import MongoClient
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hwatoo():
    hwatoo_list = ['1-1', '1-2', '2-1', '2-2', '3-1', '3-2', '4-1', '4-2', '5-1', '5-2', '6-1', '6-2', '7-1', '7-2', '8-1', '8-2', '9-1', '9-2', '10-1', '10-2']
    # hwatoo_random = random.shuffle(hwatoo_list)
    random.shuffle(hwatoo_list)
    hwatoo_selection = hwatoo_list[0:4]

    hwatoo_four = []
    for i in range(4):
        # print(type(i))
        point_split = hwatoo_selection[i].split('-')
        hwatoo_four.append(point_split[0])

    print('hwatoo_four :', hwatoo_four)
    my_sum = int(hwatoo_four[0]) + int(hwatoo_four[1])
    com_sum = int(hwatoo_four[2]) + int(hwatoo_four[3])

    my_remainder = my_sum % 10
    com_remainder = com_sum % 10

    # my_sum = int(hwatoo_selection[0].split('-')[0]) + int(hwatoo_selection[1].split('-')[0])
    # com_sum = int(hwatoo_selection[2].split('-')[0]) + int(hwatoo_selection[3].split('-')[0])
    # my_remainder = my_sum % 10
    # com_remainder = com_sum % 10

    # 판정
    winner = ''
    if my_remainder > com_remainder:
        winner = '내가 이김'
    elif my_remainder < com_remainder:
        winner = '컴퓨터 승리'
    else:
        winner = '비김'

    # print(hwatoo_selection[1])
    # print(hwatoo_selection[1].split("-"))
    # print(len(hwatoo_selection))

    return render_template('hwatoo.html', hwatoo_selection=hwatoo_selection, winner=winner, my_remainder=my_remainder, com_remainder=com_remainder)


if __name__ == '__main__':
    app.run()