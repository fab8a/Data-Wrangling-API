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
2. Limitado de set de datos a exclusivamente jugadores con *Status* actual igual a *Active* `dataset = col.find({'Status': 'Active'})`
3. Delimitación de columnas con una lista de columnas deseadas `dataframe.loc[:, columns_to_keep]`

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
