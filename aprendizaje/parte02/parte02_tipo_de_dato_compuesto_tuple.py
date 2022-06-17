# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Tipo de Dato tuple  ..............................  19-101 #
#		Acceso a los Elementos  ......................   28-53 #
#			Desempaquetamiento  ......................      37 #
#			Acceso a Índices Negativos  ..............      45 #
#		Concepto de Inmutabilidad  ...................      54 #
#		Construcción de una Tupla  ...................   69-84 #
#			MODO A  ..................................      71 #
#			MODO B  ..................................      82 #
#		Operaciones Básicas  .........................      89 #
#	Iterar Por Medio de Ciclos while  ................     102 #
#	Iterar Por Medio de Ciclos for 1/2  ..............     117 #
#	Iterar Por Medio de Ciclos for 2/2  .............. 127-143 #
#		Función `enumerate()`  .......................     136 #
# ============================================================ #

# ============================================================ #
#                       Tipo de Dato tuple                     #
# ============================================================ #

punto = (2, 5)

print('Tipo de dato `punto`:', type(punto).__name__)
print('Contenido `punto`:', punto)

# ============================================================ #
#                    Acceso a los Elementos                    #
# ============================================================ #

x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y, '\n')

# ============================================================ #
#                      Desempaquetamiento                      #
# ============================================================ #

abscisa, ordenada = punto
print('El valor en x es igual a:', abscisa)
print('El valor en y es igual a:', ordenada, '\n')

# ============================================================ #
#                  Acceso a Índices Negativos                  #
# ============================================================ #

penultimoElemento = punto[-2]
ultimoElemento = punto[-1]
print('El valor en x es igual a:', penultimoElemento)
print('El valor en y es igual a:', ultimoElemento)

# ============================================================ #
#                   Concepto de Inmutabilidad                  #
# ============================================================ #

punto = (2, 5)

# punto[0] = 3 # Genera TypeError
# punto[1] = 7 # Genera TypeError

punto = (3, 7)
x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y)

# ============================================================ #
#                   Construcción de una Tupla                  #
# ------------------------------------------------------------ #
#                            MODO A                            #
# ============================================================ #

numeros = 1, 2, 3
print('Contenido `numeros`:', numeros)

numeros = 1,
# numeros = (1,)
print('Contenido `numeros`:', numeros)

# ============================================================ #
#                            MODO B                            #
# ============================================================ #

numeros = tuple([1, 2, 3])
print('Contenido `numeros`:', numeros)

# ============================================================ #
#                      Operaciones Básicas                     #
# ============================================================ #

colores = ('Negro', 'Blanco', 'Negro', 'Azul', 'Negro', 'Rojo', 'Verde')

print('Operaciones o métodos que provee la clase `tuple`:')

print(colores.count('Negro'))
print(colores.count('Negro'))
print(colores.index('Rojo'))
print(colores.index('Negro'))

# ============================================================ #
#               Iterar Por Medio de Ciclos while               #
# ============================================================ #

numerosPrimos = (2, 3, 5, 7, 11, 13, 17, 19)

i = 0

print('\nIteración con ciclo for:')

while i < len(numerosPrimos):
    print(
        f'El valor del elemento en el indice {i} es igual a {numerosPrimos[i]}')
    i += 1

# ============================================================ #
#              Iterar Por Medio de Ciclos for 1/2              #
# ============================================================ #

print('\nIteración con ciclo for:')

for i in range(len(numerosPrimos)):
    print(
        f'El valor del elemento en el indice {i} es igual a {numerosPrimos[i]}')

# ============================================================ #
#              Iterar Por Medio de Ciclos for 2/2              #
# ============================================================ #

print('\nIteración con ciclo for mejorado:')

for n in numerosPrimos:
    print('Valor:', n)

# ============================================================ #
#                     Función `enumerate()`                    #
# ============================================================ #

print('\nIteración con la funcion enumerate():')

for i, v in enumerate(numerosPrimos):
    print(f'El valor del elemento en el indice {i} es igual a {v}')