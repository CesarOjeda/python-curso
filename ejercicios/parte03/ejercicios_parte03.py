from math import radians, pi, degrees

a = 1
b = 2
c = 3
d = 16
e = 7

# ============================================================ #
# Ejercicio 3.1. Convertir grados a radianes.                  #
# ============================================================ #

# ============================ #
# Solución 1:                  #
# ============================ #

# grados = float(input('Ingrese grados:'))

def degreesToRadians(dgr):
	result = pi * dgr / 180
	return result


# a = degreesToRadians(grados)

# print('Los grados introducidos por teclado equivalen a: {} radianes.'.format(a))

# ============================ #
# Solución 2:                  #
# ============================ #

# a = radians(grados)

# print('Los grados introducidos por teclado equivalen a: {} radianes.'.format(a))

# ============================================================ #
# Ejercicio 3.2. Convertir radianes a grados.                  #
# ============================================================ #

# ============================ #
# Solución 1:                  #
# ============================ #

# radianes = float(input('\nIngrese radianes:'))

def radiansToDegrees(rdn):
	result = 180 * rdn / pi
	return result

# b = radiansToDegrees(radianes)

# print('Los radianes introducidos por teclado equivalen a: {} grados.'.format(b))

# ============================ #
# Solución 2:                  #
# ============================ #

# b = degrees(radianes)

# print('Los radianes introducidos por teclado equivalen a: {} grados.'.format(b))

# ============================================================ #
# Ejercicio 3.3. Calcular área de un trapezoide.               #
# ============================================================ #

# baseSuperior = float(input('Ingrese base superior: '))
# baseInferior = float(input('Ingrese base inferior: '))
# altura = float(input('Ingrese altura: '))

def calculateTrapezoidArea(bs, bi, alt):
	result = (bs + bi) / 2 * alt
	return result

# c = calculateTrapezoidArea(baseSuperior, baseInferior, altura)

# print('El area del trapezoide es igual a:', c)

# ============================================================ #
# Ejercicio 3.4. Calcular el área superficial y el volumen     #
# de un cilindro.											   #
# ============================================================ #

# radio = float(input('Ingrese radio: '))
# altura = float(input('Ingrese altura: '))

def calculateSurfaceArea(rdo, alt):
	result = 2 * pi * rdo ** 2 + 2 * pi * rdo * alt
	return result

def calculateVolume(rdo, alt):
	result = pi * rdo ** 2 * alt
	return result

# d = calculateSurfaceArea(radio, altura)
# e = calculateVolume(radio, altura)

# print('El area del cilindro es:', d)
# print('El volumen del cilindro es:', e)

# ============================================================ #
# Ejercicio 3.5. Calcular el valor discriminante de una        #
# expresión cuadrática.                                        #
# ============================================================ #

# a = 1
# b = 0
# c = -1

def calculateDiscriminantValue(a, b, c):
	result = b**2 - 4*a*c
	return result

# f = calculateDiscriminantValue(a, b, c)

# print('Discriminante:', f)

# ============================================================ #
# Ejercicio 3.6. Convertir expresiones algebraicas a           #
# expresiones programáticas.								   #
# ============================================================ #

def firstAlgebraicExpression(a, b, c, d):
	result = a / (b*c) / d**(1/2)**3
	return result

def secondAlgebraicExpression(a, b, c, d, e):
	result = (a**3)**2 - b*c/(d*e)
	return result

g = firstAlgebraicExpression(a, b, c, d)
h = secondAlgebraicExpression(a, b, c, d, e)

print('Resultado:', g)

print('\nResultado:', h)