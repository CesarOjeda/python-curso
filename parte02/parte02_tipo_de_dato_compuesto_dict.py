# 1. Creación de diccionarios:

diccionario_1 = {'propiedad1': 1, 'propiedad2': 2, 'propiedad3': [1, 2, 3]}
diccionario_2 = dict()
diccionario_2['propiedad1'] = 1
diccionario_2['propiedad2'] = 2
diccionario_2['propiedad3'] = [1, 2, 3]

print('Contenido `diccionario_1`:', diccionario_1)
print('Tipo de dato `diccionario_1`:', type(diccionario_1))

print('\nContenido `diccionario_2`:', diccionario_2)

# 1.1 Creación de un Diccionario para Representar los Datos de un Computador

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}
              
print(computador)

print(f'La variable diccionario `computador` tiene {len(computador)} propiedades.')

print('Tipo de dato `computador`: %s' % type(computador).__name__)

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 2. Acceso a las propiedades y valores de un diccionario:

print('Acceso a las propiedades y valores de un diccionario:')
print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['ram']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")
print('\nCantidad de propiedades del diccionario `computador`:', len(computador))

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 2.1. Acceso a las propiedades y valores de un diccionario:

print(computador.get('Almacenamiento', '1'))
print(computador.get('tarjeta_grafica', 'integrada'))

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 3. Modificación del contenido de un diccionario:

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

# 4. Iterar un Diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 4.1. Iterar un Diccionario por sus Llaves

for k in computador.keys():
    print(f'{k.upper()} : {computador[k]}')

# 4. Iterar un Diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 4.2. Iterar un Diccionario por los Valores de las Llaves

for v in computador.values():
    print(v)

"""### Llave y Valor"""

# 4. Iterar un Diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 4.3. Iterar un Diccionario por Cada Llave y Valor

for k, v in computador.items():
    print(f'{k.upper()} : {v}')

# 5. Métodos y operadores para variables de tipo diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 5.1. list(): para convertir las llaves de un diccionario en una lista

atributos = list(computador)

print(atributos)
print('Cantidad de llaves (atributos) del diccionario `computador`:', len(atributos))

# 5. Métodos y operadores para variables de tipo diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 5.2. in: para consultar si una llave se encuentra en un diccionario:
print('in: para consultar si una llave se encuentra en un diccionario:\n')

print('¿Se encuentra la Board en el computador?\n>', 'board' in computador)

print('¿Se encuentra la CPU en el computador?\n>', 'cpu' in computador)

# 5. Métodos y operadores para variables de tipo diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 5.3. pop(): extrae un elemento del diccionario
print('pop(): extrae un elemento del diccionario:\n')

print('¿Se encuentra la CPU en el computador?\n>', 'cpu' in computador)

valor = computador.pop('cpu')

print('\nSe ha removido la llave `cpu` del diccionario `computador`.')
print('El valor de la llave `cpu` era:', valor)
print('\n¿Se encuentra la CPU en el computador?\n>', 'cpu' in computador)

valor = computador.pop('cpu', 'Dispositivo no presente en el computador.')
print('\n{}'.format(valor))

# computador.pop('diskette') # Genera KeyError

# 5. Métodos y operadores para variables de tipo diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 5.4. popitem(): extrae un elemento (llave, valor) del diccionario siguiendo un esquema LIFO:

print('Contenido: {}'.format(computador))

atributo = computador.popitem()

print('\nContenido: {}'.format(atributo))

print('Llave: {}'.format(atributo[0]))
print('Valor: {}'.format(atributo[1]))

# 5. Métodos y operadores para variables de tipo diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 5.5 reversed(): invierte el orden de las llaves del diccionario:

print('reversed():', 'invierte el orden de las llaves del diccionario:\n'.upper())
print('Lista de llaves:', list(computador))
print('\nLista de llaves invertidas: {}\n'.format(list(reversed(computador))))

for k in computador:
    print(f'{k.upper()} : {computador[k]}')
    
print('\n:)...\n')

for k in reversed(computador):
    print(f'{k.upper()} : {computador[k]}')

# 5. Métodos y operadores para variables de tipo diccionario

computador = {'id': 1001,
              'marca': 'MSi',
              'ram': 128,
              'cpu': 'Intel Core i7 Extreme Edition',
              'almacenamiento': 8}

# 5.6 clear(): remueve todos los elementos de un diccionario:
print('clear(): remueve todos los elementos de un diccionario.\n')

computador.clear()

print('Cantidad actual de llaves en el diccionario `computador`:', len(computador))
