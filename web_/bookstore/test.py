import base64

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

myclient = MyMongoClient()
