import requests
from pymongo import MongoClient
import config

client = MongoClient(f'mongodb+srv://{config.username}:{config.password}@cluster101.ryj3opk.mongodb.net/?retryWrites=true&w=majority') 
database = config.database
collection = config.collection

if database in client.list_database_names():
    print(f'{database} is already populated in MongoDB.')
    client.close()
else:
    response = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Players?key=76ef6fbf494e4afabcfdb8669644c1cf')
    if response.status_code == 200:
        # Reespuesta exitosa de solicitud a API -> guardar contenido como JSON 
        data = response.json()

        client = MongoClient(f'mongodb+srv://{config.username}:{config.password}@cluster101.ryj3opk.mongodb.net/?retryWrites=true&w=majority')
        db = client[database]
        col = db[collection]
        col.insert_many(data)
        print('Data written into MongoDB.')
    else:
        print('Error ocurred while making the API request.')
    client.close()

