import requests, json, os
from pymongo import MongoClient
import config

client = MongoClient(f'mongodb+srv://{config.username}:{config.password}@cluster101.ryj3opk.mongodb.net/?retryWrites=true&w=majority') 
db = client[config.database]
col = db[config.collection]
dataset = col.find({})[0]


