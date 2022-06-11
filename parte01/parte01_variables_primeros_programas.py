# ============================================================ #
#							  INDICE						   #
# ------------------------------------------------------------ #
#	Variables  ..........................................   12 #
#	Consultas de Tipo de Dato  ..........................   23 #
#	Variables para Representar/Guardar Texto  ...........   43 #
#	Concatenación  ......................................   60 #
#	Primeros Programas 1/2  .............................   86 #
#	Primeros Programas 2/2  .............................  102 #
# ============================================================ #

# ============================================================ #
# Variables		   											   #
# ============================================================ #

edad = 18
diasVividos = edad * 365

print('La edad almacenada en la variable `edad` es:\n> {}'.format(edad))
print('Según la edad almacenada en la variable `edad` usted ha vivido:\n> {} días.'.format(diasVividos))

# ============================================================ #
# Consultas de Tipo de Dato 	   							   #
# ============================================================ #

edad = 18
diasVividos = edad * 365

print('La edad almacenada en la variable `edad` es:\n> {}'.format(edad))
print('Según la edad almacenada en la variable `edad` usted ha vivido:\n> {} días.\n'.format(diasVividos))

print('La variable `edad` es de tipo: {}.'.format(type(edad)))
print('La variable `diasVividos` es de tipo: {}.\n'.format(type(diasVividos)))

print('El ID Único(o posición en memoría) de la variable `edad` es: {}.'.format(id(edad)))
print('El ID Único(o posición en memoría) de la variable `diasVividos` es: {}.\n'.format(id(diasVividos)))

print('La posición en memoría del valor `18` es: {}.'.format(id(18)))
print('La posición en memoría del valor `6570` es: {}.'.format(id(6570)))

# ============================================================ #
# Estudio y Comprensión de las Variables para Guardar y        #
# Representar Texto											   #
# ============================================================ #

nombre = 'César'
apellido = "Ojeda"
nombreCompleto = nombre + ' ' + apellido

print('Su nombre es:', nombre)
print('Su apellido es:', apellido)
print('Su nombre completo es:', nombreCompleto)

print('\nLa variable `nombre` es de tipo: {}.'.format(type(nombre)))
print('La variable `apellido` es de tipo: {}.'.format(type(apellido)))
print('La variable `nombreCompleto` es de tipo: {}.'.format(type(nombreCompleto)))

# ============================================================ #
# Variables para Representar/Guardar Texto              	   #
# ============================================================ #

nombre = '\nCésar'
apellido = "Ojeda"
nombreCompleto = nombre + ' ' + apellido

print('Su nombre es:', nombre)
print('Su apellido es:', apellido)
print('Su nombre completo es:', nombreCompleto)

print('\nLa variable `nombre` es de tipo: {}.'.format(type(nombre)))
print('La variable `apellido` es de tipo: {}.'.format(type(apellido)))
print('La variable `nombreCompleto` es de tipo: {}.'.format(type(nombreCompleto)))

edad = 18
nombreEdad = nombreCompleto + ' tiene ' + str(edad) + ' años.'

print(nombreEdad)

nombreEdad = '{} tiene {} años.'.format(nombreCompleto, edad)

print(nombreEdad)

# ============================================================ #
# Primeros Programas 1/2                            		   #
# ============================================================ #

def sumar(a, b):
	suma = a + b
	return suma

# n1 = int(input('Ingrese el primer número:\n> '))
# n2 = int(input('Ingrese el segundo número:\n> '))

# resultado = sumar(n1, n2)

# print('La suma de {} y {} da como resultado:\n> {}'.format(n1, n2, resultado))

# ============================================================ #
# Primeros Programas 2/2							 		   #
# ============================================================ #

def sumar(a, b):
	suma = a + b
	return suma

# n1 = float(input('Ingrese el primer número:\n> '))
# n2 = float(input('Ingrese el segundo número:\n> '))

# resultado = sumar(n1, n2)

# print('La suma de {} y {} da como resultado:\n> {}'.format(n1, n2, resultado))
