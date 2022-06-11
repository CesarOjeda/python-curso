# ============================================================ #
#							  INDICE						   #
# ------------------------------------------------------------ #
#	Tipo de Dato int  ...................................   17 #
#		Construccion de Valor Numerico Entero  ..........   27 #
#		Operaciones Básicas  ............................   37 #
#	Tipo de Dato float  .................................   56 #
#		Construccion de Valor Numerico Flotante  ........   69 #
#		Operaciones Básicas  ............................   78 #
#	Tipo de Dato complex  ...............................   91 #
#		Operaciones Básicas  ............................  103 #
#	Tipo de Dato boolean  ...............................  121 #
#		Construccion de Valor Booleano  .................  144 #
#		Operaciones Básicas  ............................  158 #
# ============================================================ #

# ============================================================ #
#                       Tipo de Dato int                       #
# ============================================================ #

puntaje = 300
x = -5

print('La variable `puntaje` es de tipo: {}.'.format(type(puntaje)))
print('La variable `x` es de tipo: {}.'.format(type(x)))

# ============================================================ #
#             Construccion de Valor Numerico Entero            #
# ============================================================ #

edad = int(input('Ingrese su edad: '))
print('\nLa variable `edad` es de tipo:: %s\n' % type(edad))

dias_vividos = edad * 365
print('Según la edad almacenada en la variable `edad` usted ha vivido: %i días.' % dias_vividos)

# ============================================================ #
#                      Operaciones Básicas                     #
# ============================================================ #

puntaje = 300

print('Puntaje antes de la adición 50 puntos: %i' % puntaje)

puntaje = puntaje + 50

print('Puntaje después de la adición 50 puntos: %i' % puntaje)

x = -5

print('Valor de x antes de la adición: %i' % x)
x += 10 # x = x + 10
print('Valor de x después de la adición: %i' % x)
print('La variable `x` es de tipo: %s' % type(x))

# ============================================================ #
#                      Tipo de Dato float                      #
# ============================================================ #

pi = 3.1415
precio = 23.95

print('Valor de `pi`: %.4f' % pi)
print('Valor de `precio`: %.2f\n' % precio)

print('La variable `pi` es de tipo: {}'.format(type(pi).__name__))
print('La variable `precio` es de tipo:', type(precio).__name__)

# ============================================================ #
#            Construccion de Valor Numerico Flotante           #
# ============================================================ #

precioProducto = float(input('Digite el precio del producto: '))
print('La variable `precioProducto` es de tipo: {}'.format(type(precioProducto).__name__))

print('El producto cuesta: ${}'.format(precioProducto))

# ============================================================ #
#                      Operaciones Básicas                     #
# ============================================================ #

pi = 3.1415
precio = 29.95

pi = pi * 2
print('El nuevo valor de la variable `pi` es:', pi)

total = precio * 5
print('\nEl total de la compra es: %.2f' % total)

# ============================================================ #
#                     Tipo de Dato complex                     #
# ============================================================ #

numeroComplejo = 2 - 3j
print('Contenido `numeroComplejo`: {}\n'.format(numeroComplejo))
print('Tipo de dato `numeroComplejo` es: {}\n'.format(type(numeroComplejo).__name__))

numeroComplejoDos = complex(2, -3)
print('Contenido `numeroComplejoDos`: {}\n'.format(numeroComplejoDos))
print('Tipo de dato `numeroComplejoDos`: {}\n'.format(type(numeroComplejoDos).__name__))

# ============================================================ #
#                      Operaciones Básicas                     #
# ============================================================ #

print('Operaciones aritmeticas sobre numeros complejos\n')

suma = 2 - 3j + (1 + 5j)
print('La suma de estos numeros complejos da como resultado: {}\n'.format(suma))

resta = 2 - 3j - complex(1, 5)
print('La resta de estos numeros complejos da como resultado: {}\n'.format(resta))

producto = 2 - 3j * (1 + 5j)
print('El producto de estos numeros complejos da como resultado: {}\n'.format(producto))

division = 2 - 3j / (1 + 5j)
print('La division de estos numeros complejos da como resultado: {}'.format(division))

# ============================================================ #
#                     Tipo de Dato boolean                     #
# ============================================================ #

llueve = False
print('Tipo de dato `llueve`:', type(llueve).__name__)
print('Contenido `llueve`:', llueve)

if llueve:
	print('El día está lluvioso.')
else:
	print('El día no está esplendido.')

llueveDos = not llueve

print('\nTipo de dato de la variable `llueveDos` es:', type(llueveDos).__name__)
print('Contenido `llueveDos`:', llueveDos)

if llueveDos:
	print('El día está lluvioso.')
else:
	print('El día no está esplendido.')

# ============================================================ #
#                Construccion de Valor Booleano                #
# ============================================================ #

print('Uso de la clase bool() para crear valores logicos:\n')

numOne = bool(1)
print('Tipo de dato `numOne`: {}'.format(type(numOne).__name__))
print('Contenido `numOne`: {}\n'.format(numOne))

numTwo = bool(0)
print('Tipo de dato `numTwo`: {}'.format(type(numTwo).__name__))
print('Contenido `numTwo`: {}'.format(numTwo))

# ============================================================ #
#                      Operaciones Básicas                     #
# ============================================================ #

llaveUno = True
llaveDos = False

print(llaveUno and llaveDos,'\n')
print(llaveUno and not llaveDos,'\n')
print(llaveDos or llaveUno,'\n')
print(llaveDos or not llaveUno,'\n')

if llaveUno:
	print('Si hay agua.')
else:
	print('No hay agua.')

if llaveUno and llaveDos:
	print('Si hay agua.')
else:
	print('No hay agua.')

if llaveUno and not llaveDos:
	print('Si hay agua.')
else:
	print('No hay agua.')

if llaveUno or llaveDos:
	print('Si hay agua.')
else:
	print('No hay agua.')

if llaveUno or not llaveDos:
	print('Si hay agua.')
else:
	print('No hay agua.')

if not llaveUno or llaveDos:
	print('Si hay agua.')
else:
	print('No hay agua.')
