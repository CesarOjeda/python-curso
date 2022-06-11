from sys import version, version_info
from datetime import datetime
from math import pi

# ============================================================= #
# Ejercicio 1.1 - Versión Actual de Python Instalada en el      #
# Sistema                                                       #
# ============================================================= #
 
def versionActual():
	return f'Su Versión de Python es: {version}'

def infoVersion():
	return 'Información de Versión: {}'.format(version_info)

a = versionActual()
b = infoVersion()

# ~ print(a)
# ~ print(b)

# ============================================================= #
# Ejercicio 1.2 - Obtener la Fecha y Hora Actuales del			#
# Sistema										                #
# ============================================================= #

def fechaHoraActual():
	fechaHoraActual = datetime.now()
	return f'Fecha y Hora Actual en el Sistema: {fechaHoraActual}'

def fechaHoraFormateada():
	fechaHoraFormateada = datetime.now().strftime('%H:%M:%S %Y/%m/%d')
	return f'Fecha y Hora Formateada en el Sistema: {fechaHoraFormateada}'

c = fechaHoraActual()
d = fechaHoraFormateada()

# ~ print(c)
# ~ print(d)

# ============================================================= #
# Ejercicio 1.3 - Calcular el Área de un Círculo Dado el 		#
# Radio 										                #
# Formula: pi * r ^ 2											#
# ============================================================= #

# radio = float(input('Ingrese el radio del circulo: '))

def calcAreaCirculo(r):
	area = pi * r ** 2
	return area

# e = calcAreaCirculo(radio)

# print('El area es igual a:', e)

# ============================================================= #
# Ejercicio 1.4 - Invertir el Orden de los Caracteres de una	#
# Palabra      												    #
# ============================================================= #

# palabra = input('Ingrese palabra a invertir: ')

def invertirPalabra(p):
	palabraInvertida = p[::-1]
	return palabraInvertida

# f = invertirPalabra(palabra)

# print('Palabra Invertida:', f)

# ============================================================= #
# Ejercicio 1.5 - Calcular el Área de un Triángulo Dadas la		#
# Base y la Altura 											    #
# ============================================================= #

# base = float(input('Ingrese base del triángulo:'))
# altura = float(input('Ingrese altura del triángulo:'))

def calcAreaTriangulo(b, a):
	area = b * a / 2
	return area

# g = calcAreaTriangulo(base, altura)

# print('El área del triángulo es igual a: {}'.format(g))
