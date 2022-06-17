from random import choice
from heapq import nlargest
from json import dumps
from collections import Counter

listaNumeros = [2, 4, 6, 8, 10]

tuplaNumeros = (2, 4, 6, 8, 10)
tuplaLenguajesProgramacion = ('Python', 'JavaScript', 'Perl', 'C++', 'Java')

listaNumerosDuplicados = [1, 2, 3, 1, 1, 1, 4, 5, 6, 3, 3, 2, 5]
listaPaises = ['Colombia', 'Perú', 'Alemania', 'Estados Unidos', 'China', 'Argentina', 'Irán', 'Irak']
elementosAleatorios = list(range(1, 101))

diccionarioProductos = {
	'Mouse': 29.9,
	'Teclado': 119.7,
	'Audífonos': 35.3,
	'Monitor': 277
}
diccionarioElementosDuplicados = {
	1001: 'Mouse',
	1002: 'Teclado', 
	1003: 'Monitor', 
	1004: 'Mouse',
	1005: 'Audífonos',
	1006: 'Teclado'
}

arcoiris = {'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul', 'Añil'}
colores = {'Rojo', 'Verde', 'Azul', 'Negros', 'Rosa'}
escritorio = {'Notepad++', 'Atom', 'Eclipse', 'NetBeans', 'PyCharm'}
portatil = {'Notepad++', 'PyCharm', 'Visual Studio Code', 'IntelliJ IDEA'}

# ============================ #
# EJERCICIOS TUPLAS:           #
# ============================ #

# ============================================================ #
# Ejercicio 1.1. Convertir una lista en una tupla.             #
# ============================================================ #

a = tuple(listaNumeros)

# print('Contenido `lista_numeros`:', a)

# ============================================================ #
# Ejercicio 1.2. Invertir el contenido de una tupla.           #
# ============================================================ #

# ============================ #
# Solución 1:                  #
# ============================ #

def invertirTupla(t):
	tuplaInvertida = []
	for i in range(len(t) - 1, -1, -1):
		tuplaInvertida.append(t[i])
	return tuplaInvertida

b = tuple(invertirTupla(tuplaNumeros))

# print('Contenido `tuplaNumeros`:', b)

# ============================ #
# Solución 2:                  #
# ============================ #

b = tuple(reversed(tuplaNumeros))

# print('Contenido `tuplaNumeros`:', b)

# ============================================================ #
# Ejercicio 1.3. Crear una sección de una tupla usando         #
# notación de slicing (rebanado).                              #
# ============================================================ #

c = tuplaNumeros[0:3]

# print('Contenido `tuplaNumeros`:', c)

# ============================================================ #
# Ejercicio 2.1.4. Remover un elemento (valor) de una tupla.   #
# ============================================================ #

def removerElementosTuplas(lr, tlp):
	if lr in tlp:
		tlp = tlp[0:2] + tlp[3:]
		return f'Contenido `tuplaLenguajesProgramacion`: {tlp}'
	else:
		return f'No existe el nombre de lenguaje que usted indico: {lr}'

d = removerElementosTuplas('Perl', tuplaLenguajesProgramacion)

# print('Contenido `tuplaLenguajesProgramacion`:', d)

# ============================ #
# EJERCICIOS LISTAS:           #
# ============================ #

# ============================================================ #
# Ejercicio 2.1. Remover los valores duplicados en una         #
# lista.                                                       #
# ============================================================ #

# ============================ #
# Solución 1:                  #
# ============================ #

def removerDuplicadosLista(lnd):
	duplicadosRemovidos = []

	for n in lnd:
		if n not in duplicadosRemovidos:
			duplicadosRemovidos.append(n)
	return duplicadosRemovidos

e = removerDuplicadosLista(listaNumerosDuplicados)

# print('Contenido `listaNumerosDuplicados`:', e)

# ============================ #
# Solución 2:                  #
# ============================ #

duplicadosRemovidos = list(set(listaNumerosDuplicados))

# print('Contenido `listaNumerosDuplicados`:', duplicadosRemovidos)

# ============================================================ #
# Ejercicio 2.2. Encontrar las palabras de una lista que       #
# tienen al menos 5 caracteres de longitud.                    #
# ============================================================ #

def encontrarPalabras(lp):
	paisesCaracteres = []

	for p in lp:
		if len(p) >= 5:
			paisesCaracteres.append(p)
	return paisesCaracteres

f = encontrarPalabras(listaPaises)

# print('Contenido `paisesCaracteres`:', f)

# ============================ #
# Solución 2:                  #
# ============================ #

paisesCaracteres = [p for p in listaPaises if len(p) >= 5]

# print('Contenido `paisesCaracteres`:', paisesCaracteres)

# ============================================================ #
# Ejercicio 2.3. Seleccionar de forma aleatoria un elemento    #
# de una lista.												   #
# ============================================================ #

elemento = choice(elementosAleatorios)

# print('Contenido `elemento`:', elemento)

# ============================================================ #
# Ejercicio 2.4. Calcular la frecuencia (ocurrencias) de los   #
# elementos de una lista.                                      #
# ============================================================ #

def calcOcurrencias(o):
	ocurrencias = {}

	for n in o:
		if n in ocurrencias:
			ocurrencias[n] += 1
		else:
			ocurrencias[n] = 1
	return ocurrencias

g = calcOcurrencias(listaNumerosDuplicados)

# print('Contenido `listaNumerosDuplicados`:', g)

# ============================ #
# EJERCICIOS DICCIONARIOS:     #
# ============================ #

# ============================================================ #
# Ejercicio 3.1:.Sumar todos los valores de un diccionario.    #
# ============================================================ #

totalProductos = sum(diccionarioProductos.values())

# print('Total a pagar:', totalProductos)

# ============================================================ #
# Ejercicio 3.2. Remover todos los elementos duplicados de     #
# un diccionario.                                              #
# ============================================================ #

def removerDuplicadosDiccionarios(ded):
	diccionarioProductosUnicos = {}

	for k, v in ded.items():
		if v not in diccionarioProductosUnicos.values():
			diccionarioProductosUnicos[k] = v
	return diccionarioProductosUnicos

h = removerDuplicadosDiccionarios(diccionarioElementosDuplicados)

# print('Contenido `diccionarioElementosDuplicados`:', h)

# ============================================================ #
# Ejercicio 3.3. Encontrar los tres valores mayores en un      #
# diccionario.												   #
# ============================================================ #

productosCaros = nlargest(3, diccionarioProductos, key=diccionarioProductos.get)

# print('Los tres productos más caros son:', productosCaros)

# ============================================================ #
# Ejercicio 3.4. Convertir un diccionario en su                #
# representación en el formato JSON.                           #
# ============================================================ #

productosJson = dumps(diccionarioProductos)

# print('Contenido `productosJson`:', productosJson)

# ============================ #
# EJERCICIOS CONJUNTOS:        #
# ============================ #

# ============================================================ #
# Ejercicio 4.1. Realizar operaciones de unión e               #
# intersección de conjuntos.                                   #
# ============================================================ #

unionColores = arcoiris.union(colores)
interseccion = colores.intersection(arcoiris)

# print('Contenido `unionColores`: {}'.format(unionColores))
# print('Contenido `interseccion`: {}'.format(interseccion))

# ============================================================ #
# Ejercicio 4.2. Calcular la diferencia entre dos 	    	   #
# conjuntos.									               #
# ============================================================ #

resultado = escritorio.difference(portatil)

# print('Los programas que hacen falta en el computador portátil son:', resultado)
# resultado = portatil.difference(escritorio)
# print('\nLos programas que hacen falta en el computador de escritorio son:', resultado)

# ============================================================ #
# Ejercicio 4.3. Calcular la diferencia simétrica entre        #
# dos conjuntos.    										   #
# ============================================================ #

resultado = escritorio.symmetric_difference(portatil)

# print('Contenido `resultado`:', resultado)
