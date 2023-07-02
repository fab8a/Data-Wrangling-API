# Data-Wrangling-API
- Code repository for the Data Wrangling module's project of the Data Science course from the Dev.F platform.
- Repositorio de codigo del proyecto perteneciente al modulo de Data Wrangling para el curso de Data Science por parte de Dev.F
--- 

## Desarrollo del proyecto

### Data sourcing [data_sourcing.py]
1. Obtención de datos
	- Registro como desarrollador en el portal de [SportsData.io](https://sportsdata.io/developers/api-documentation/nfl#/sports-data)
	- Solicitud a la NFL API para obtencion del total de jugadores actuales. [NFL Players Details by Available](https://api.sportsdata.io/v3/nfl/scores/json/Players?key=76ef6fbf494e4afabcfdb8669644c1cf)
2. Escritura a base de datos
	- Conexión a MongoDB mediante cliente de *pymongo*
 	- Inserción de los datos como un JSON a una nueva coleccion dentro de una nueva base de datos

### Data cleaning
1. Obtencion de datos mediante una consulta en una nueva conexion al cliente de MongoDB
2. Limitado de set de datos a exclusivamente jugadores con *Status* actual igual a *Active*: `dataset = col.find({'Status': 'Active'})`
3. Delimitación de columnas con una lista de columnas deseadas: `dataframe.loc[:, columns_to_keep]`

### API declaration [main.py]
1. Iniciación de app con el web framework *[FastAPI](https://fastapi.tiangolo.com/)*
2. Creación de logica mediante uso de Pandas DataFrames para las respuestas en multiples casos
3. Declaración de endpoints y su retorno respectivo para cada caso
4. [Documentación](https://datawapi-1-p1826191.deta.app/docs)

### API hosting [Spacefile]
- La API se encuentra alojada como un script de Python en la plataforma de Cloud Computing *'[Deta Space](https://deta.space/)'*
- El archivo [Spacefile](https://deta.space/docs/en/build/reference/spacefile) define las características del proyecto **Space**
- Despliegue de aplicaciones de [FastAPI en Deta Space](https://fastapi.tiangolo.com/deployment/deta/)
- La plataforma asigna un URL genérico por el cual se puede acceder a la API. https://datawapi-1-p1826191.deta.app/
- Uno de los beneficios de FastAPI es la generacion automatica de [Documentacion](https://datawapi-1-p1826191.deta.app/docs) completa para la API

---


## Project Development
### Data sourcing [data_sourcing.py]
1. Data acquisition
	- Registered as a developer on the [SportsData.io](https://sportsdata.io/developers/api-documentation/nfl#/sports-data) portal
	- Made a request to the NFL API in order to obtain the [total number of current players](https://api.sportsdata.io/v3/nfl/scores/json/Players?key=76ef6fbf494e4afabcfdb8669644c1cf).
2. Writing to the database
	- Connected to MongoDB using the pymongo client
	- Inserted the data as a JSON into a new collection within a new database

### Data cleaning
1. Retrieveed data through a query in a new connection to the MongoDB client
2. Limited the dataset to only players with the current *Status* equal to *Active*: `dataset = col.find({'Status': 'Active'})`
3. Column delimitation with a list of desired columns: `dataframe.loc[:, columns_to_keep]`


### API declaration [main.py]
1. Initialized the app with the *[FastAPI](https://fastapi.tiangolo.com/)* web framework
2. Created the logic for multiple request cases using Pandas DataFrames for the response
3. Declared the endpoints and their respective return for each case
4. [Documentation](https://datawapi-1-p1826191.deta.app/docs)


### API hosting [Spacefile]
- The API is hosted as a Python script on the Cloud Computing platform *'[Deta Space](https://deta.space/)'*
- The file [Spacefile](https://deta.space/docs/en/build/reference/spacefile) defines the characteristics of the Space project
- Deploying [FastAPI apps on Deta Space](https://fastapi.tiangolo.com/deployment/deta/)
- The platform assigns a generic URL through which the API can be accessed: https://datawapi-1-p1826191.deta.app/
- One of the benefits of FastAPI is the automatic generation of complete [documentation](https://datawapi-1-p1826191.deta.app/docs) for the API

---

## Extras
- List of options to pass as the parameter {team}. [NFL teams abbreviation codes](https://operations.nfl.com/the-rules/2022-nfl-rulebook/#abbreviation-codes)
- List of options to pass as the parameter {position} (G replaces OL, and DB is the aggregate of CB and S). [NFL abbreviation legend](https://newsday.sportsdirectinc.com/football/nfl-matchups-glossary.aspx)
- The {weight} parameter represents pounds of weight.
