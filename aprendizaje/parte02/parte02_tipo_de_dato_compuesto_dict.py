# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Tipo de Dato dict  ...............................  21-151 #
#		Construcción de Diccionarios  ................      23 #
#		Acceso a las Propiedades y Valores  ..........      48 #
#		Modificación  ................................      63 #
#		Métodos y Operadores  ........................  80-151 #
#			`list()` Convierte las Llaves en Listas  .      82 #
#			`in` Operación de Pertenencia  ...........      91 #
#			`pop()` Extrae Elementos  ................     101 #
#			`popitem()` Sigue el Esquema LIFO  .......     120 #
#			`reversed()` Invierte las Llaves  ........     133 #
#			`clear()` El Diccionario Queda Vacio  ....     141 #
#	Iterar Por Medio de Ciclos for  .................. 152-179 #
#		por sus Llaves  ..............................     154 #
#		por los Valores de las Llaves  ...............     161 #
#		por Cada Llave y Valor  ......................     168 #
# ============================================================ #

# ============================================================ #
#                       Tipo de Dato dict                      #
# ============================================================ #
#                 Construcción de Diccionarios                 #
# ============================================================ #

diccionarioUno = {'propiedadUno': 1, 'propiedadDos': 2, 'propiedadTres': [1, 2, 3]}
diccionarioDos = dict()
diccionarioDos['propiedadUno'] = 1
diccionarioDos['propiedadDos'] = 2
diccionarioDos['propiedadTres'] = [1, 2, 3]

print('Contenido `diccionarioUno`:', diccionarioUno)
print('Tipo de dato `diccionarioUno`:', type(diccionarioUno))

print('\nContenido `diccionarioDos`:', diccionarioDos)

computador = {
				'id': 1001,
				'marca': 'MSi',
				'ram': 128,
				'cpu': 'Intel Core i7 Extreme Edition',
				'almacenamiento': 8
			  }
							
print(computador)

# ============================================================ #
#              Acceso a las Propiedades y Valores              #
# ============================================================ #

print('Acceso a las propiedades y valores de un diccionario:')
print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['ram']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")
print('\nCantidad de propiedades del diccionario `computador`:', len(computador))

print(computador.get('Almacenamiento', '1'))
print(computador.get('tarjeta_grafica', 'integrada'))

# ============================================================ #
#                         Modificación                         #
# ============================================================ #

computador['marca'] = 'Alienware'
computador['id'] = '2001'
computador['gpu'] = 'NVIDIA GeForce RTX 2080 8GB'

print('Modificación del contenido de un diccionario:')
print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['ram']}")
print(f"CPU: {computador['cpu']}")
print(f"GPU: {computador['gpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")
print('\nCantidad de propiedades del diccionario `computador`:', len(computador))

# ============================================================ #
#                     Métodos y Operadores                     #
# ============================================================ #
#            `list()` Convierte las Llaves en Listas           #
# ============================================================ #

atributos = list(computador)

print(atributos)
print('Cantidad de llaves (atributos) del diccionario `computador`:', len(atributos))

# ============================================================ #
#                 `in` Operación de Pertenencia                #
# ============================================================ #

print('in: para consultar si una llave se encuentra en un diccionario:\n')

print('¿Se encuentra la Board en el computador?\n>', 'board' in computador)

print('¿Se encuentra la CPU en el computador?\n>', 'cpu' in computador)

# ============================================================ #
#                   `pop()` Extrae Elementos                   #
# ============================================================ #

print('pop(): extrae un elemento del diccionario:\n')

print('¿Se encuentra la CPU en el computador?\n>', 'cpu' in computador)

valor = computador.pop('cpu')

print('\nSe ha removido la llave `cpu` del diccionario `computador`.')
print('El valor de la llave `cpu` era:', valor)
print('\n¿Se encuentra la CPU en el computador?\n>', 'cpu' in computador)

valor = computador.pop('cpu', 'Dispositivo no presente en el computador.')
print('\n{}'.format(valor))

# computador.pop('diskette') # Genera KeyError

# ============================================================ #
#               `popitem()` Sigue el Esquema LIFO              #
# ============================================================ #

print('Contenido: {}'.format(computador))

atributo = computador.popitem()

print('\nContenido: {}'.format(atributo))

print('Llave: {}'.format(atributo[0]))
print('Valor: {}'.format(atributo[1]))

# ============================================================ #
#               `reversed()` Invierte las Llaves               #
# ============================================================ #

print('reversed():', 'invierte el orden de las llaves del diccionario:\n'.upper())
print('Lista de llaves:', list(computador))
print('\nLista de llaves invertidas: {}\n'.format(list(reversed(computador))))

# ============================================================ #
#             `clear()` El Diccionario Queda Vacio             #
# ============================================================ #

print('clear(): remueve todos los elementos de un diccionario.\n')

computador.clear()

print('Cantidad actual de llaves en el diccionario `computador`:', len(computador))


# ============================================================ #
#                Iterar Por Medio de Ciclos for                #
# ============================================================ #
#                        por sus Llaves                        #
# ============================================================ #

for k in computador.keys():
		print(f'{k.upper()} : {computador[k]}')

# ============================================================ #
#                 por los Valores de las Llaves                #
# ============================================================ #

for v in computador.values():
		print(v)

# ============================================================ #
#                    por Cada Llave y Valor                    #
# ============================================================ #

for k, v in computador.items():
		print(f'{k.upper()} : {v}')

for k in computador:
		print(f'{k.upper()} : {computador[k]}')

for k in reversed(computador):
		print(f'{k.upper()} : {computador[k]}')