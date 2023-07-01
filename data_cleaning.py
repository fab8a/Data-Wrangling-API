import requests, json, os
import pandas as pd
from pymongo import MongoClient
import config

client = MongoClient(f'mongodb+srv://{config.username}:{config.password}@cluster101.ryj3opk.mongodb.net/?retryWrites=true&w=majority') 
db = client[config.database]
col = db[config.collection]

dataset = col.find({'Status': 'Active'})
df = pd.json_normalize(dataset)

columns_to_keep = ['Name', 'Team', 'Position', 'Age', 'Height', 'Weight', 'College', 'CollegeDraftYear']
df_selected = df.loc[:, columns_to_keep]
data = df_selected

json_data = data.to_json(orient='records')
data = eval(json_data)

db = client[config.database]
col = db['NFL_players_cleaned']
col.insert_many(data)
print('Data written into MongoDB.')
client.close()