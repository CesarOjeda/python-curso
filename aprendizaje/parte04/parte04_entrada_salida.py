# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Entrada de Datos (Input)  ........................       ? #
#	Salida de Datos (Output)  ........................       ? #
#		Múltiples Argumentos para `print()`  .........       ? #
#		Desempaquetamiento de una Colección  .........       ? #
# ============================================================ #

# ============================================================ #
#                   Entrada de Datos (Input)                   #
# ============================================================ #

try:
    nombre = input('Digite su nombre: ')

    print('El tipo de dato de la variable `nombre` es:', type(nombre).__name__)
    print('El contenido de la variable `nombre` es:', nombre)
except EOFError:
    print('El usuario ha cancelado la introducción de datos.')
    print('El nombre de la persona no se capturó.')

print('El programa ha finalizado de forma satisfactoria.')

# ============================================================ #
#                   Salida de Datos (Output)                   #
# ============================================================ #

nombre = 'John Ortiz Ordoñez'
edad = 29

print('Nombre: ' + nombre, end=' - ')
print('Edad: ' + str(edad))

print('\nAprendiendo el uso de la', end=' ')
print('función print()')

# ============================================================ #
#             Múltiples Argumentos para `print()`              #
# ============================================================ #

email = 'john@mail.co'

print(nombre, edad, email)

print(nombre, edad, email, sep='')
print(nombre, edad, email, sep=' - ')

lenguajes = ('Python', 'JavaScript', 'C++', 'C#', 'Java')

print('\n', lenguajes)
print(lenguajes[0], lenguajes[1], lenguajes[2], lenguajes[3], lenguajes[4], sep=' - ')

# ============================================================ #
#             Desempaquetamiento de una Colección              #
# ============================================================ #

print('\n', *lenguajes, sep=' - ')