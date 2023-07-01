import json, config
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pymongo import MongoClient

app = FastAPI()
client = MongoClient(f'mongodb+srv://{config.username}:{config.password}@cluster101.ryj3opk.mongodb.net/?retryWrites=true&w=majority') 
db = client[config.database]
col = db[config.collection]

dataset = col.find({'Status': 'Active'})
df = pd.json_normalize(dataset)

columns_to_keep = ['Name', 'Team', 'Position', 'Age', 'Height', 'Weight', 'College', 'CollegeDraftYear']
df_selected = df.loc[:, columns_to_keep]
data = df_selected
client.close()

@app.get('/')
async def root():
    return {'example':'Root of the NFL players API'}

@app.get('/active')
async def get_active():
    active: int = int(data.count()[0])
    return {'Number of active players in the NFL:': active}

@app.get('/active_per_team/{team}')
async def get_active_team(team: str):
    # Amount of Active players for a certain team {team}
    active_per_team = int(data[data['Team'] == team].count()[0])
    return {f"Amount of Active players for {team}": active_per_team}

@app.get('/active_per_position/{position}')
async def get_active_position(position: str):
    # Amount of Active players for a certain position {position}
    active_per_position = int(data[data['Position'] == position].count()[0])
    return {f"Amount of Active players playing {position}": active_per_position}

@app.get('/oldest_player/{limit}')
async def get_oldest(limit: int):
    # Oldest players in the league {amount}
    oldest_players = data.sort_values('Age', ascending=False).head(limit)
    json_oldest = oldest_players.to_json(orient='records')
    return JSONResponse(content=json_oldest) 

@app.get('/heaviest_player/{position}/{limit}')
async def get_heaviest(position: str, limit: int):
    heaviest_players = data.sort_values('Weight', ascending=False)
    heaviest_limited = heaviest_players[heaviest_players['Position'] == position].head(limit)
    json_heaviest = heaviest_limited.to_json(orient='records')
    return JSONResponse(content=json_heaviest) 

@app.get('/lightest_player/{position}/{limit}')
async def get_lightest(position: str, limit: int):
    lightest_player = data.sort_values('Weight')
    lightest_limited = lightest_player[lightest_player['Position'] == position].head(limit)
    json_lightest = lightest_limited.to_json(orient='records')
    return JSONResponse(content=json_lightest) 

@app.get('/above_weight/{weight}')
async def get_above_weight(weight: int):
    # Amount of players above a certain weight {pounds}
    above_weight = int(data[data['Weight'] >= weight].count()[0])
    return {f"Amount of Active players weighing more than {weight} pounds": above_weight}
