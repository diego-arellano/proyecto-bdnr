#! /home/diego/miniconda3/envs/bddnr/bin/python

import requests
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["swapi"]
list=["films", "people", "planets", "species", "starships", "vehicles"]

for table in list:
	collection = my_db[table]
	url = "https://swapi.dev/api/"+table+"/"
	i = 1
	j = 0
	request = requests.get(url)
	response = request.json()
	limite = response["count"]
	print(limite)
	res = []
	while j <= limite :
		request = requests.get(url+str(i))
		if request.status_code != 404:
			j+=1
			response = request.json()
			collection.insert_one(response)
			print(j)
		i+=1
