#!/usr/bin/python3
import requests
import json

#Función para pedir los datos del usuario
#Bucle para asegurar poner el nombre del municipio en el formato correcto
#Primera letra mayúscula y resto minúscula

def readData():
	cap_municipio=None
	
	print("Introduce el municipio en el que vives: ")
	municipio=input()	

	for i, c in enumerate(municipio): 
		if not c.isdigit():
			break
			
	return municipio[:i] + municipio[i:].capitalize()
		
#Obnetemos los datos de la API con get y los parseamos a json
def getData(url):
	req=requests.get(url).json()
	return req

#Función que devuelve los datos en relación a los campos pasado por parámetros
#response es la lista de los datos 
# key1 es la clave primera
# value1 es el nombre del municipio
# key2 es la segunda clave 

def findData(response,key1,value1,key2):
	for dat in response :
		if dat[key1] == value1 : 
			return dat[key2]


#Funcion que muestra los resultados
def printResult(data,value):
	print(f"Temperatura {data} : {value}")


def wheather():

	#Obtenemos los datos de los  municipios para obtener el código provincia
	data1= getData("https://www.el-tiempo.net/api/json/v2/municipios")

	#Excepción por si el dato introducido no es correcto o no se encuentra el municipio
	#Todo en bucle hasta que el resultado para mostrar en pantalla sea correcto
	while True: 
		municipio=readData()
		codprov=findData(data1,"NOMBRE",municipio,"CODPROV")
		try:
			temperatures=getData("https://www.el-tiempo.net/api/json/v2/provincias/"+codprov)
			maxmin=findData(temperatures["ciudades"],"name",municipio,"temperatures")
			printResult("Temperatura máxima: ",maxmin["max"])
			printResult("Temperatura mínima: ",maxmin["min"])
			break
		
		except:
			print("Este municipio no se puede encontrar")



if __name__ == "__main__":
	wheather()
