import requests, json

response = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Players?key=76ef6fbf494e4afabcfdb8669644c1cf')

if response.status_code == 200:
    # If succesfull response -> get content as JSON
    data = response.json()

    with open('api_data.json', 'w') as file:
        json.dump(data, file)
    print('Datos guardados en archivo JSON.')
else:
    print('Error al realizar la peticion al API.')