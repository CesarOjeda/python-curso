# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Introducción a los Ciclos/Bucles  ................       ? #
#	Ciclos `for`  ....................................       ? #
#		Manera Explicita  ............................       ? #
#		Ejemplo 1. Suma de los Números Pares  ........       ? #
#		Ejemplo 2. Suma de los Números Impares  ......       ? #
#		Listas de Compresión  ........................       ? #
#			Simplificar el Proceso de Sumar  .........       ? #
#			Simplificar el Proceso de Sumar Pares  ...       ? #
#			Simplificar el Proceso de Sumar Impares  .       ? #
#		Iteración por Índice y Valor  ................       ? #
#	Ciclos `while`  ..................................       ? #
#		Suma de los Elementos de una Lista  ..........       ? #
#		Suma de los Valores Pares  ...................       ? #
#		Suma de los Valores Impares  .................       ? #
#		Terminación Arbitraria  ......................       ? #
# ============================================================ #

# ============================================================ #
#               Introducción a los Ciclos/Bucles               #
# ============================================================ #

numeros = [1, 2, 3, 4, 5]

total = 0

total = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
print('Total de la suma de los números de 1 a 5:', total)

total = 0

total += numeros[0]
total += numeros[1]
total += numeros[2]
total += numeros[3]
total += numeros[4]
# total += numeros[999]
print('\nTotal de la suma de los números de 1 a 5:', total)

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print('\nContenido actual de la lista `numeros`:', numeros)

total += numeros[5]
total += numeros[6]
total += numeros[7]
total += numeros[8]
total += numeros[9]

print('Total de la suma de los números de 1 a 10:', total)

# ============================================================ #
#                         Ciclos `for`                         #
# ============================================================ #
#                       Manera Explicita                       #
# ============================================================ #

total = 0

for i in range(0, len(numeros)):
	total += numeros[i]

print('Total de la suma de los números de 1 a 10:', total)

# ============================================================ #
#                   Ciclos `for` (Mejorado)                    #
# ============================================================ #

total = 0

for n in numeros:
	print('El valor actual de `n` es', n)
	total += n

print('Total de la suma de los números de 1 a 10:', total)

# ============================================================ #
#             Ejemplo 1. Suma de los Números Pares             #
# ============================================================ #

sumaPares = 0

for i in range(len(numeros)):
	if numeros[i] % 2 == 0:
		sumaPares += numeros[i]

print('La suma de los números pares que hay en la lista `numeros` es igual a', sumaPares)

# ============================================================ #
#       Ejemplo 1. Suma de los Números Pares (Mejorado)        #
# ============================================================ #

sumaPares = 0

for n in numeros:
	if n % 2 == 0:
		sumaPares += n

print('La suma de los números pares que hay en la lista `numeros` es igual a', sumaPares)

# ============================================================ #
#           Ejemplo 2. Suma de los Números Impares             #
# ============================================================ #

sumaImpares = 0

for i in range(len(numeros)):
	if numeros[i] % 2 == 1:
		sumaImpares += numeros[i]

print('La suma de los números impares que hay en la lista `numeros` es igual a', sumaImpares)

# ============================================================ #
#      Ejemplo 2. Suma de los Números Impares (Mejorado)       #
# ============================================================ #

sumaImpares = 0

for n in numeros:
	if n % 2 == 1:
		sumaImpares += n

print('La suma de los números impares que hay en la lista `numeros` es igual a', sumaImpares)

# ============================================================ #
#                     Listas de Compresión                     #
# ============================================================ #
#               Simplificar el Proceso de Sumar                #
# ============================================================ #

numeros = [1, 2, 3, 4, 5]

total = [numeros[i] for i in range(len(numeros))]

print('Contenido de la variable `total`:', total)

total = sum([numeros[i] for i in range(len(numeros))])

print('El total de la suma de los números de 1 a 10 es igual a', total)

# ============================================================ #
#            Simplificar el Proceso de Sumar Pares             #
# ============================================================ #

print('Suma pares usando una lista de comprensión:')

pares = [numeros[i] for i in range(len(numeros)) if numeros[i] % 2 == 0]

print('Contenido de la variable `pares`:', pares)
print('Tipo de dato de la variable `pares`:', type(pares))

suma_pares = sum(pares)

print('La suma de los números pares es igual a:', suma_pares)

# ============================================================ #
#           Simplificar el Proceso de Sumar Impares            #
# ============================================================ #

print('\nSuma impares usando una lista de comprensión:')

impares = [numeros[i] for i in range(len(numeros)) if numeros[i] % 2 == 1]

print('Contenido de la variable `impares`:', impares)
print('Tipo de dato de la variable `impares`:', type(impares))

suma_impares = sum(impares)

print('La suma de los números impares es igual a:', suma_impares)

# ============================================================ #
#                 Iteración por Índice y Valor                 #
# ============================================================ #

for i, n in enumerate(numeros):
	print('Índice: %i - Valor: %i' % (i, n))

# ============================================================ #
#                        Ciclos `while`                        #
# ============================================================ #

i = 0

while i < len(numeros):
	print(numeros[i])
	i += 1

print('Contenido de la lista `numeros`:', numeros)

# ============================================================ #
#              Suma de los Elementos de una Lista              #
# ============================================================ #

i = 0
total = 0

while i < len(numeros):
    total += numeros[i]
    i += 1

print('Suma de los números de 1 a 5:', total)

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print('\nContenido de la lista `numeros`:', numeros)

# ============================================================ #
#                  Suma de los Valores Pares                   #
# ============================================================ #

suma_pares = 0
i = 0

while i < len(numeros):
    if numeros[i] % 2 == 0:
        suma_pares += numeros[i]
    i += 1

print('Suma de todos los valores pares que hay en el rango 1-10:', suma_pares)

# ============================================================ #
#                 Suma de los Valores Impares                  #
# ============================================================ #

suma_impares = 0
i = 0

while i < len(numeros):

    if numeros[i] % 2 != 0:
        suma_impares += numeros[i]

    i += 1

print('Suma de los valores impares en el rango 1 a 10:', suma_impares)

# ============================================================ #
#                    Terminación Arbitraria                    #
# ============================================================ #

total = 0

while True:
    numero = int(input('Escriba un número entero positivo (un número igual o menor a cero para terminar): '))

    if numero <= 0:
        break
    
    total += numero

print('El acumulado en total es igual a', total)