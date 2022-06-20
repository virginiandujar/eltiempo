# eltiempo

**Programa python que a partir del nombre del municipio obtienes las temperaturas máximas y mínimas**

 - Para ejecutar el programa sería:
    python3 tiempo.py

 - Nada más ejecutarlo, pide al usuario un nombre de municipio.
 
		"Introduce el municipio en el que vives:"
		GETAFE

- El usuario puede introducir el municipio en mayúsuculas o minúsculas, el programa lo cambia al formato adecuado para compararlo con los datos que se obtienen de la API.

- Si el dato introducido es un número o ese municipio no se encuentra, el programa recoge la excepción y vuelve a pedir al usuario que introduzca el municipio, así hasta que lo encuentre.
El programa devolverá al usuario la temperatura máxima y mínima del munipio elegido.

		Introduce el municipio en el que vives:
		1
		Este municipio no se puede encontrar
		Introduce el municipio en el que vives:
		ARGANDA
		Este municipio no se puede encontrar
		Introduce el municipio en el que vives:
		GETAFE
		Temperatura Temperatura máxima:  : 29
		Temperatura Temperatura mínima:  : 16









