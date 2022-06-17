# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Tipo de Dato set  ................................  22-231 #
#		Construcción de Conjuntos  ...................   24-63 #
#			a Partir de una Cadena de Caracteres  ....      40 #
#			a Partir de una Tupla  ...................      51 #
#		Métodos y Operadores  ........................  64-231 #
#			`add()` Agregar Elementos  ...............      70 #
#			`in` Operación de Pertenencia  ...........      84 #
#			`issubset()` Operación de Subconjunto  ...     100 #
#			`union()` Unión entre Conjuntos  .........     126 #
#			`intersection()` Intersección  ...........     138 #
#			`issuperset()` Superconjunto  ............     150 #
#			Diferencia de Conjuntos  .................     170 #
#			Diferencia Simétrica  ....................     189 #
#			Remover Elementos  .......................     200 #
#	Iterar Por Medio de Ciclos for  .................. 232-250 #
#		Función `enumerate()`  .......................     241 #
# ============================================================ #

# ============================================================ #
#                       Tipo de Dato set                       #
# ============================================================ #
#                   Construcción de Conjuntos                  #
# ============================================================ #

print('Creación de Conjuntos\n')

conjuntoOne = {'Juan', 'Oliva', 'Edward', 'Daniela', 'Juan', 'Juan', 'Germán'}
conjuntoTwo = set(['Juan', 'Oliva', 'Edward',
				 'Daniela', 'Juan', 'Juan', 'Germán'])

print('Contenido `conjuntoOne`: {}'.format(conjuntoOne))
print('Tipo de dato `conjuntoOne`: {}\n'.format(type(conjuntoTwo).__name__))

print('Contenido `conjuntoTwo`: {}'.format(conjuntoTwo))
print('Tipo de dato `conjuntoTwo`: {}'.format(type(conjuntoTwo).__name__))

# ============================================================ #
#             a Partir de una Cadena de Caracteres             #
# ============================================================ #

frase = 'Python es un lenguaje de programación'
print('Contenido `frase`: {}'.format(frase))

caracteres = set(frase)

print('Contenido `caracteres`: {}'.format(caracteres))

# ============================================================ #
#                     a Partir de una Tupla                    #
# ============================================================ #

primos = (7, 3, 5, 2, 7, 5, 13, 11, 19, 2, 2, 2, 5, 5)
primosUnicos = set(primos)

print('Contenido `primos`: {}'.format(primos))
print('Tipo de dato `primos`: {}\n'.format(type(primos).__name__))

print('Contenido `primosUnicos`: {}'.format(primosUnicos))
print('Tipo de dato `primosUnicos`: {}'.format(type(primosUnicos).__name__))

# ============================================================ #
#                     Métodos y Operadores                     #
# ============================================================ #

arcoiris = {'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul', 'Añil'}

# ============================================================ #
#                   `add()` Agregar Elementos                  #
# ============================================================ #

arcoiris.add('Violeta')

print('Contenido (despues) `arcoiris`: {}'.format(arcoiris))

arcoiris.add('Violeta')
arcoiris.add('Violeta')

print('Contenido (despues) `arcoiris`: {}'.format(arcoiris))
print('Cantidad de elementos (despues) `arcoiris`: {}\n'.format(len(arcoiris)))

# ============================================================ #
#                 `in` Operación de Pertenencia                #
# ============================================================ #

print('Operación de Pertenencia en un Conjunto\n')

color = 'Gris'
result = color in arcoiris

print('¿El color {} se encuentra del arcoíris?\n> {}\n'.format(color, result))

color = 'Naranja'
result = color in arcoiris

print('¿El color {} se encuentra del arcoíris?\n> {}'.format(color, result))

# ============================================================ #
#             `issubset()` Operación de Subconjunto            #
# ============================================================ #

coloresOne = {'Rojo', 'Verde', 'Azul'}
coloresTwo = {'Rojo', 'Verde', 'Azul'}

result_one = coloresOne.issubset(arcoiris)

coloresTwo.add('Gris')
resultTwo = coloresTwo.issubset(arcoiris)

empty = set([])
result_three = empty.issubset(arcoiris)

print('Operación de Subconjunto en un Conjunto\n')

print('¿El conjunto {} es subconjunto de {}?\n> {}\n'.format(
	coloresOne, arcoiris, result_one))

print('¿El conjunto {} es subconjunto de {}?\n> {}\n'.format(
	coloresTwo, arcoiris, resultTwo))

print('¿El conjunto {} es subconjunto de {}?\n> {}'.format(
	empty, arcoiris, result_three))

# ============================================================ #
#                `union()` Unión entre Conjuntos               #
# ============================================================ #

colores = {'Rojo', 'Verde', 'Azul', 'Negros', 'Rosa'}

print('Operaciones de Unión entre Conjuntos\n')

unionColores = arcoiris.union(colores)

print('Contenido `unionColores`: {}'.format(unionColores))

# ============================================================ #
#                 `intersection()` Intersección                #
# ============================================================ #

print('Operaciones de Intersección entre Conjuntos\n')

interseccion = colores.intersection(arcoiris)

print('Contenido `interseccion`: {}'.format(interseccion))
print('Cantidad de elementos `interseccion`: {}'.format(len(interseccion)))
print('Tipo de dato `interseccion`: {}'.format(type(interseccion).__name__))

# ============================================================ #
#                 `issuperset()` Superconjunto                 #
# ============================================================ #

coloresRgb = {'Rojo', 'Verde', 'Azul'}

print('Operación de Superconjunto\n')

resultado = arcoiris.issuperset(coloresRgb)

print('¿El conjunto {} es superconjunto de {}?\n> {}'.format(
	arcoiris, coloresRgb, resultado))

coloresRgb.add('Gris')

resultado = arcoiris.issuperset(coloresRgb)

print('¿El conjunto {} es superconjunto de {}?\n> {}'.format(
	arcoiris, coloresRgb, resultado))

# ============================================================ #
#                    Diferencia de Conjuntos                   #
# ============================================================ #

print('Diferencia de Conjuntos\n')

# A = {1, 2, 3}
# B = {3, 4, 5}
# C = A - B = {1, 2}
# D = B - A = {4, 5}

diferencia = colores - arcoiris

print('La diferencia entre los conjuntos `colores` y `arcoiris` es: {}'.format(diferencia))

diferencia = arcoiris - colores

print('La diferencia entre los conjuntos `arcoiris` y `colores` es: {}'.format(diferencia))

# ============================================================ #
#                     Diferencia Simétrica                     #
# ============================================================ #

print('Diferencia Simétrica\n')

diferenciaSimetrica = arcoiris.symmetric_difference(colores)

print('La diferencia simétrica entre los conjuntos `arco_iris` y `colores` es:',
	  diferenciaSimetrica)

# ============================================================ #
#                       Remover Elementos                      #
# ============================================================ #



colores.remove('Rojo')

print('\nContenido `colores`:', colores)

# colores.remove('gris') # Genera KeyError

# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ #

pop = {'Rojo', 'Verde', 'Azul', 'Negro', 'Rosa'}

color = pop.pop()

print('\nEl color removido fue:', color)

print('\nContenido `pop`:', pop)

# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ #

clear = {'Rojo', 'Verde', 'Azul', 'Negro', 'Rosa'}

colores.clear()

print('Contenido `clear`:', clear)

# colores.pop() # Genera error KeyError: el conjunto está vacío.

# ============================================================ #
#                Iterar Por Medio de Ciclos for                #
# ============================================================ #

print('Iterar o Recorrer un Conjunto')

for c in arcoiris:
	print('Color {}'.format(c))

# ============================================================ #
#                     Función `enumerate()`                    #
# ============================================================ #

print('Iterar o Recorrer un Conjunto con la Función `enumerate()`\n')

for i, c in enumerate(arcoiris):
	print(f'Índice: {i} - Valor: {c}')

# NOTA IMPORTANTE: En un conjunto no existe la noción o el concepto de orden.