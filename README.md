# proyecto-bdnr

# <link> https://ugeek.github.io/blog/post/2020-05-27-copiar-directorios-o-archivos-de-un-docker-a-local-o-viceversa.html
# Api utilizada: <link> https://swapi.py4e.com/documentation

# Agregué al script de conv_csv la siguiente instrucción dentro de cada for: 
#docker cp ./$col.csv monetdb:/swapi_csv
# Para después poder ejecutar dentro de monet las siguientes instrucciones:
# Crear la tabla necesaria para cada una de las tablas 
#copy offset 2 into people from '/swapi_csv/people.csv' on client using delimiters ',',E'\n',E'\"' null as ' ';

#Nota: es importante checar la parte de los delimitadores todavía, porque las comas dentro de los arreglos están ocasionando serios problemas para copiar el csv a monet

# Agregué los comandos necesarios para crear la base de datos en neo4j 

#+begin_src bash
docker stop mongo
docker rm mongo

export DATA_DIR=`pwd`/data
echo $DATA_DIR
export EX_DIR=`pwd`/mongodb-sample-dataset
echo $EX_DIR
mkdir -p $DATA_DIR
docker run -p 27017:27017 \
       -v $DATA_DIR:/data/db \
       -v $EX_DIR:/mongodb-sample-dataset \
       --name mongo \
       -d mongo

#+end_src

#+begin_src python
import requests
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
my_db = client["swapi"]
list=["starships", "vehicles", "species", "films", "planets", "people"]

for table in list:
    collection = my_db[table]
    url = "https://swapi.py4e.com/api/"+table+"/"
    i = 1
    j = 1
    request = requests.get(url)
    response = request.json()
    limite = response["count"]
    print(limite)
    res = []
    
    while j <= limite:
        url_i = url + str(i)
        req = requests.get(url_i)
        if req.status_code != 404:
            resp = req.json()
            res.append(resp)
            print(j)
            j+=1
        i+=1
    print("fin de tabla"+table)
    collection.insert_many(res)
#+end_src

