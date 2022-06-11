# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Tipo de Dato list  ...............................       ? #
#	    Acceso a los Elementos  ......................       ? #
#	        Acceso a Índices Positivos  ..............       ? #
#	        Acceso a Índices Negativos  ..............       ? #
#	        Acceso a Subsecciones  ...................       ? #
#	        Desempaquetamiento  ......................       ? #
#	        Acceso a Índice no Existente  ............       ? #
#	            Indices Habilitados  .................       ? #
#	            ERROR  ...............................       ? #
#       Modificación  ................................       ? #
#           Índices Positivos  .......................       ? #
#           Índices Negativos  .......................       ? #
#       Métodos  .....................................       ? #
#           Inserción de Elementos  ..................       ? #
#           Remoción de Elementos  ...................       ? #
#           `count()` Contar las Ocurrencias  ........       ? #
#           `reverse()` Inversión del Contenido  .....       ? #
#	Iterar Por Medio de Ciclos while  ................       ? #
#	Iterar Por Medio de Ciclos for  ..................       ? #
# ============================================================ #

# ============================================================ #
#                       Tipo de Dato list                      #
# ============================================================ #
#                    Acceso a los Elementos                    #
# ============================================================ #

numeros = [2, 4, 6, 8, 10]

print('Contenido `numeros`:', numeros)

# ============================================================ #
#                  Acceso a Índices Positivos                  #
# ============================================================ #

dos = numeros[0]
print('El Primer Elemento (Índice 0) De La Lista Es:', dos)

diez = numeros[4]
print(f'El Último Elemento (Índice 4) De La Lista Es: {diez}\n')

# ============================================================ #
#                  Acceso a Índices Negativos                  #
# ============================================================ #

diez = numeros[-1]
print('El Último Elemento (Índice -1) De La Lista Es: {}\n'.format(diez))

# ============================================================ #
#                     Acceso a Subsecciones                    #
# ============================================================ #

subseccion = numeros[1:4]

print('Contenido `subseccion`: {}\n'.format(subseccion))

# ============================================================ #
#                      Desempaquetamiento                      #
# ============================================================ #

cuatro, seis, ocho = subseccion

print(f'[{ocho}, {seis}, {cuatro}]')

# ============================================================ #
#                 Acceso a Índice no Existente                 #
# ============================================================ #
#                      Indices Habilitados                     #
# ============================================================ #

# Izquierda A Derecha: 0 hasta n - 1
# Derecha A Izquierda: -1 hasta -n

# ============================================================ #
#                             ERROR                            #
# ============================================================ #

# valor = numeros[8] # Genera ValueError
# valor = numeros[-6] # Genera ValueError

# ============================================================ #
#                         Modificación                         #
# ============================================================ #
#                       Índices Positivos                      #
# ============================================================ #

print(f'El primer elemento (Índice 0) de la lista es: {numeros[0]}\n')

numeros[0] = 1

print(f'El primer elemento (Índice 0) de la lista es: {numeros[0]}\n')

# ============================================================ #
#                       Índices Negativos                      #
# ============================================================ #

print(
    'El último elemento (Índice -1) de la lista es: {}\n'.format(numeros[-1]))

numeros[-1] = 12



print(
    'El último elemento (Índice -1) de la lista es: {}\n'.format(numeros[-1]))

print('Contenido (Despues) `numeros`: {}'.format(numeros))

# ============================================================ #
#                            Métodos                           #
# ============================================================ #
#                    Inserción de Elementos                    #
# ============================================================ #

print('Inserción de elementos por medio del metodo `append()`\n')

numeros.append(14)
numeros.append(16)
print('Contenido actual `numeros`:', numeros)

# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ #

print('\nInserción de elementos por medio del metodo `insert()`\n')

numeros.insert(1, 2)

print('Contenido actual `numeros`:', numeros)

numeros.insert(-1, 15)

print('\nContenido actual `numeros`:', numeros)

# ============================================================ #
#                     Remoción de Elementos                    #
# ============================================================ #

print('Remover elemento con la funcion `remove()`')

print('Contenido actual `numeros`:', numeros)

numeros.remove(2)

print('Contenido actual `numeros`:', numeros)

# numeros.remove(1) # Genera ValueError

# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ #

print('Remover elementos con la funcion `pop()`')

ultimo_elemento = numeros.pop()

print(f'\nSe ha eliminado {ultimo_elemento} de la lista `numeros`')

ocho = numeros.pop(numeros.index(8))

print(f'\nSe ha eliminado {ocho} de la lista `numeros`')
print('\nContenido actual `numeros`:', numeros)

ultimo_elemento = numeros.pop(-1)

print(f'\nSe ha eliminado {ultimo_elemento} de la lista `numeros`')
print('\nContenido actual `numeros`:', numeros)

# numeros.pop(20) # Genera IndexError

# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ #

print('Eliminación de todos los elementos de una lista con el método `clear()`:')
print('\nCantidad actual de elementos `numeros`:', len(numeros))
numeros.clear() # Equivale a: del numeros[:]
print('\nCantidad actual de elementos `numeros`:', len(numeros))

# ============================================================ #
#               `count()` Contar las Ocurrencias               #
# ============================================================ #

print('Uso del método `count()` para contar las ocurrencias de un elemento en una lista:')

numeros.append(14)
numeros.append(14)
numeros.append(14)

ocurrencias = numeros.count(14)

print('\nCantidad de veces que se halla 14 en la lista `numeros`: %i' % ocurrencias)
print('Contenido actual `numeros`:', numeros)

ocurrencias = numeros.count(0)
print('\nCantidad de veces que se halla 0 en la lista `numeros`: %i' % ocurrencias)
print('Contenido actual `numeros`:', numeros)

# ============================================================ #
#              `reverse()` Inversión del Contenido             #
# ============================================================ #

print('Inversión del contenido de una lista con la función `reverse()`:')

print('\nContenido actual `numeros`:', numeros)
numeros.reverse()
print('\nContenido actual `numeros`:', numeros)

# ============================================================ #
#               Iterar Por Medio de Ciclos while               #
# ============================================================ #

print('\nIteración de Listas (Ciclo while):')

i = 0

while i < len(numeros):
    print(f'\nÍndice: {i} - Valor: {numeros[i]}')
    i += 1

print('\nIteración de Listas (Ciclo while del último elemento al primero):')

i = len(numeros) - 1

while i >= 0:
    print(f'\nÍndice: {i} - Valor: {numeros[i]}')
    i -= 1

# ============================================================ #
#                Iterar Por Medio de Ciclos for                #
# ============================================================ #

print('Iteracion de Listas (Ciclo for):')

for i in range(0, len(numeros)):
    print(f'\nIndice: {i} - Valor: {numeros[i]}')

print('\nIteracion de Listas (Ciclo for del ultimo elemento al primero):')

for i in range(len(numeros) - 1, -1, -1):
    print(f'\nIndice: {i} - Valor: {numeros[i]}')

print('\nIteración Elemento por Elemento de una Lista (Ciclo for):')

for n in numeros:
    print('\nValor: {}'.format(n))

print('\nIteración por Índice y Elemento de una Lista (Ciclo for):')
print('Funcion `enumerate()`')

for i, v in enumerate(numeros):
    print(f'\nIndice: {i} - Valor: {v}')
