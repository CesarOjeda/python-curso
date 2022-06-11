# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Tipo de Dato set  ................................       ? #
#	    Construcción de Conjuntos  ...................       ? #
#	        a Partir de una Cadena de Caracteres  ....       ? #
#	        a Partir de una Tupla  ...................       ? #
#	    Métodos y Operadores  ........................       ? #
#	        `add()` Agregar Elementos  ...............       ? #
#	        `in` Operación de Pertenencia  ...........       ? #
#	        `issubset()` Operación de Subconjunto  ...       ? #
#	        `union()` Unión entre Conjuntos  .........       ? #
#	        `intersection()` Intersección  ...........       ? #
#	        `issuperset()` Superconjunto  ............       ? #
#	        Diferencia de Conjuntos  .................       ? #
#	        Diferencia Simétrica  ....................       ? #
#	        Remover Elementos  .......................       ? #
#   Iterar Por Medio de Ciclos for  ..................       ? #
#       Función `enumerate()`  .......................       ? #
# ============================================================ #

# ============================================================ #
#                       Tipo de Dato set                       #
# ============================================================ #
#                   Construcción de Conjuntos                  #
# ============================================================ #

print('Creación de Conjuntos\n')

conjunto_1 = {'Juan', 'Oliva', 'Edward', 'Daniela', 'Juan', 'Juan', 'Germán'}
conjunto_2 = set(['Juan', 'Oliva', 'Edward',
                 'Daniela', 'Juan', 'Juan', 'Germán'])

print('Contenido `conjunto_1`: {}'.format(conjunto_1))
print('Tipo de dato `conjunto_1`: {}\n'.format(type(conjunto_2).__name__))

print('Contenido `conjunto_2`: {}'.format(conjunto_2))
print('Tipo de dato `conjunto_2`: {}'.format(type(conjunto_2).__name__))

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

colores_one = {'Rojo', 'Verde', 'Azul'}
colores_two = {'Rojo', 'Verde', 'Azul'}

result_one = colores_one.issubset(arcoiris)

colores_two.add('Gris')
result_two = colores_two.issubset(arcoiris)

empty = set([])
result_three = empty.issubset(arcoiris)

print('Operación de Subconjunto en un Conjunto\n')

print('¿El conjunto {} es subconjunto de {}?\n> {}\n'.format(
    colores_one, arcoiris, result_one))

print('¿El conjunto {} es subconjunto de {}?\n> {}\n'.format(
    colores_two, arcoiris, result_two))

print('¿El conjunto {} es subconjunto de {}?\n> {}'.format(
    empty, arcoiris, result_three))

# ============================================================ #
#                `union()` Unión entre Conjuntos               #
# ============================================================ #

colores = {'Rojo', 'Verde', 'Azul', 'Negros', 'Rosa'}

print('Operaciones de Unión entre Conjuntos\n')

union_colores = arcoiris.union(colores)

print('Contenido `union_colores`: {}'.format(union_colores))

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

colores_rgb = {'Rojo', 'Verde', 'Azul'}

print('Operación de Superconjunto\n')

resultado = arcoiris.issuperset(colores_rgb)

print('¿El conjunto {} es superconjunto de {}?\n> {}'.format(
    arcoiris, colores_rgb, resultado))

colores_rgb.add('Gris')

resultado = arcoiris.issuperset(colores_rgb)

print('¿El conjunto {} es superconjunto de {}?\n> {}'.format(
    arcoiris, colores_rgb, resultado))

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

diferencia_simetrica = arcoiris.symmetric_difference(colores)

print('La diferencia simétrica entre los conjuntos `arco_iris` y `colores` es:',
      diferencia_simetrica)

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
