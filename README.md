# proyecto-bdnr

## Star Wars - api:
# <link> https://ugeek.github.io/blog/post/2020-05-27-copiar-directorios-o-archivos-de-un-docker-a-local-o-viceversa.html
# Api utilizada: <link> https://swapi.py4e.com/documentation

# Agregué al script de conv_csv la siguiente instrucción dentro de cada for: 
#docker cp ./$col.csv monetdb:/swapi_csv
# Para después poder ejecutar dentro de monet las siguientes instrucciones:
# Crear la tabla necesaria para cada una de las tablas 
#copy offset 2 into people from '/swapi_csv/people.csv' on client using delimiters ',',E'\n',E'\"' null as ' ';

#Nota: es importante checar la parte de los delimitadores todavía, porque las comas dentro de los arreglos están ocasionando serios problemas para copiar el csv a monet

# Agregué los comandos necesarios para crear la base de datos en neo4j 
