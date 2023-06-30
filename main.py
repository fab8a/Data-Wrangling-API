import json, config
import pandas as pd
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient(f'mongodb+srv://{config.username}:{config.password}@cluster101.ryj3opk.mongodb.net/?retryWrites=true&w=majority') 
db = client[config.database]
col = db[config.collection]
dataset = col.find({})[0]
print(dataset)

for document in dataset:
    json_data = json.dumps(document)
data = json.loads(json_data)
client.close()

@app.get('/')
async def root():
    return {'example':'Root of the API', 'data': 1000}

@app.get('/active')
async def get_active():
    data = pd.DataFrame(data)
    data = data[data['Active']].count()[0] 
    return data