# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Introducción a las Funciones  ....................       ? #
#		Obtener Documentación/Ayuda de una Función  ..       ? #
#		Ejemplo 1. Intercambio de Valores  ...........       ? #
#		Uso de Funcionalidades por Default  ..........       ? #
#	Pasar Argumentos por Valor y por Referencia  .....       ? #
#		Pasar Argumentos por Valor  ..................       ? #
#		Pasar Argumentos por Referencia  .............       ? #
#	Lista Variable de Argumentos  ....................       ? #
#	Parámetros/Argumentos Nombrados Variables  .......       ? #
#	Parámetros/Argumentos por Default  ...............       ? #
#	Funciones Recursivas  ............................       ? #
#		Ejemplo 1. Función Fibonacci  ................       ? #
#	Funciones Anónimas  ..............................       ? #
#		Filtrar Contenido de una Lista  ..............       ? #
#		Crear Mapeo de un Iterable  ..................       ? #
# ============================================================ #

# ============================================================ #
#                 Introducción a las Funciones                 #
# ============================================================ #

def sumar(n1, n2):
    """
    Suma dos números (sean enteros o punto flotante).

    Parameters:
    n1: primer valor a sumar.
    n2: segundo valor a sumar.

    Returns:
    Suma de dos números (enteros o reales).
    """
    suma = n1 + n2

    return suma

x = 2
y = 3

resultado = sumar(x, y)
print('El resultado de sumar {} y {} es igual a {}.'.format(x, y, resultado))

# ============================================================ #
#          Obtener Documentación/Ayuda de una Función          #
# ============================================================ #

help(sumar)

help(print)

# ============================================================ #
#              Ejemplo 1. Intercambio de Valores               #
# ============================================================ #

# a = 2, b = 3
# a = 3, b = 2

# auxiliar = 2
# a = 3
# b = 2

def intercambiar_valores(a, b):
    """
    Intercambia los valores de dos variables.

    Parameters:
    a: primer valor.
    b: segundo valor.

    Returns:
    Los valores de a y b intercambiados.
    """
    auxiliar = a
    a = b
    b = auxiliar

    return a, b


x = 2
b = 3

print('Valores de las variables `x` e `y` antes del intercambio:')
print(f'x = {x} - y = {y}')

resultado = intercambiar_valores(x, b)

x = resultado[0]
y = resultado[1]

print('Valores de las variables `x` e `y` después del intercambio:')
print(f'x = {x} - y = {y}')

# ============================================================ #
#              Uso de Funcionalidades por Default              #
# ============================================================ #

x = 2
y = 3

resultado = x + y
print('El resultado de sumar {} y {} es igual a {}.'.format(x, y, resultado))

print('Valores de las variables `x` e `y` antes del intercambio:')
print(f'x = {x} - y = {y}')

x, y = y, x

print('Valores de las variables `x` e `y` antes del intercambio:')
print(f'x = {x} - y = {y}')

# ============================================================ #
#         Pasar Argumentos por Valor y por Referencia          #
# ============================================================ #
#                  Pasar Argumentos por Valor                  #
# ============================================================ #

def duplicar(numero):
    numero *= 2 # numero = numero * 2
    print('El número duplicado es igual a:', numero)

x = 2
print('El valor de la variable `x` antes de su duplicación:', x)

duplicar(x)

print('El valor de la variable `x` después de su duplicación:', x)

# ============================================================ #
#               Pasar Argumentos por Referencia                #
# ============================================================ #

def agregar_elemento(lista):
    lista.append(2)

numeros = [1]
print('Contenido de la variable `numeros` antes de invocar `agregar_elemento`:', numeros)

agregar_elemento(numeros)

print('Contenido de la variable `numeros` después de invocar `agregar_elemento`:', numeros)

# ============================================================ #
#                 Lista Variable de Argumentos                 #
# ============================================================ #

# def sumar(a, b):
#     return a + b

# def sumar(a, b, c):
#     return a + b + c

# def sumar(a, b, c, d):
#     return a + b + c + d

# def sumar(a, b, c, d, e):
#     return a + b + c + d + e

def sumar(*valores):
    suma = 0

    for v in valores:
        suma += v

    return suma


resultado = sumar(1)
print('El resultado de la suma es igual:', resultado)

resultado = sumar(1, 2)
print('El resultado de la suma es igual:', resultado)

resultado = sumar(1, 2, 3)
print('El resultado de la suma es igual:', resultado)

# ============================================================ #
#          Parámetros/Argumentos Nombrados Variables           #
# ============================================================ #

def mostrar_identidad(**identificacion):
    resultado = ''

    if identificacion.get('documento'):
        resultado += 'Documento: ' + identificacion.get('documento') + '\n'
    if identificacion.get('nombre'):
        resultado += 'Nombre: ' + identificacion.get('nombre') + '\n'
    if identificacion.get('apellido'):
        resultado += 'Apellido: ' + identificacion.get('apellido') + '\n'
    
    return resultado

persona = mostrar_identidad(nombre='John', apellido='Ortiz')
print('Identificación:\n', persona)

persona = mostrar_identidad(nombre='John', apellido='Ortiz', documento='123456789')
print('Identificación:\n', persona)

# ============================================================ #
#              Parámetros/Argumentos por Default               #
# ============================================================ #

def saludar(nombre, saludo='Hola', pais='Colombia'):
    """
    Saluda utilizando un saludo, un nombre y un país de procedencia.

    Parameters:
    nombre: Nombre de la persona.
    saludo: El tipo de saludo (e.g., Hola, Buenos días, Buenas tardes, Buenas noches).
    pais: Nacionalidad de la persona.

    Returns:
    Una frase con el saludo que incluye el nombre y la nacionalidad.
    """
    frase = f'{saludo}, mi nombre es {nombre}, y soy de {pais}.'

    return frase


resultado = saludar('Edward', saludo='Buenos días')

print('Resultado:', resultado)

resultado = saludar('Daniela', pais='México')
print('Resultado:', resultado)

resultado = saludar('Oliva', pais='España', saludo='Buenas noches')
print('Resultado:', resultado)

def exponenciacion(base, exponente=2):
    """
    Calcula la exponenciación de un número base respecto a un exponente.

    Parameters:
    base: Base de la exponenciación.
    exponente: Potencia de la exponenciación (valor por defecto 2).

    Returns:
    Exponenciación de una base y un exponente.
    """
    resultado = base ** exponente

    return resultado

potencia = exponenciacion(5)
print('El resultado de la exponenciación es:', potencia)

potencia = exponenciacion(10, 3)
print('El resultado de la exponenciación es:', potencia)

# ============================================================ #
#                     Funciones Recursivas                     #
# ============================================================ #

# n!
# 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorial_iterativo(n):
    """
    Calcula el factorial de un número. (Enfoque iterativo.)

    Parameters:
    n: Número de factorial a calcular.

    Returns:
    Factorial
    """
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

def factorial_recursivo(n):
    """
    Calcula el factorial de un número. (Enfoque recursivo.)

    Parameters:
    n: Número de factorial a calcular.

    Returns:
    Factorial
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


resultado = factorial_iterativo(5)
print('Factorial (iterativo):', resultado)

resultado = factorial_recursivo(5)
print('Factorial (recursivo):', resultado)

# ============================================================ #
#                 Ejemplo 1. Función Fibonacci                 #
# ============================================================ #

# 0 1 1 2 3 5 8 13 21 34 55 89...

def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo valor de la serie Fibonacci. (Enfoque iterativo.)

    Parameters:
    n: n-ésimo valor de la serie Fibonacci a calcular.

    Returns:
    Valor de la serie Fibonacci.
    """
    a = 0
    b = 1

    for i in range(n - 1):
        a, b = b, a + b
    
    return b

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo valor de la serie Fibonacci. (Enfoque recursivo.)

    Parameters:
    n: n-ésimo valor de la serie Fibonacci a calcular.

    Returns:
    Valor de la serie Fibonacci.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 2) + fibonacci_recursivo(n - 1)

resultado = fibonacci_iterativo(10)
print('Fibonacci (iterativo):', resultado)

resultado = fibonacci_recursivo(10)
print('Fibonacci (recursivo):', resultado)

# ============================================================ #
#                      Funciones Anónimas                      #
# ============================================================ #

def sumar(a, b):
	resultado = a + b
	return resultado

x = 2
y = 3

print('La suma de {} + {} es igual a {}'.format(x, y, sumar(x, y)))

sumar_lambda = lambda a, b: a + b
print('La suma de {} + {} es igual a {}'.format(x, y, sumar_lambda(x, y)))

def cuadrado(n):
	return n ** 2

cuadrado_lambda = lambda n: n ** 2

numero = 10

print('El cuadrado de {} es igual a {}'.format(numero, cuadrado(numero)))
print('El cuadrado de {} es igual a {}'.format(numero, cuadrado_lambda(numero)))

# ============================================================ #
#                Filtrar Contenido de una Lista                #
# ============================================================ #

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Contenido de la variable `numeros`:', numeros)
print('Cantidad de elementos en la lista `numeros`:', len(numeros))

def extraer_impares(lista):
	impares = []

	for n in lista:
		if n % 2 != 0:
			impares.append(n)
	
	return impares

resultado = extraer_impares(numeros)

print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

resultado = [n for n in numeros if n % 2 != 0]
print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

resultado = list(filter(lambda n: n % 2 != 0, numeros))
print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

def filtro(n):
	return n % 2 != 0

resultado = list(filter(filtro, numeros))
print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

# ============================================================ #
#                  Crear Mapeo de un Iterable                  #
# ============================================================ #

def elevar_cuadrado(lista):
	cuadrados = []

	for n in lista:
		cuadrados.append(n ** 2)
	
	return cuadrados

resultado = elevar_cuadrado(numeros)
print('Contenido de la variable `numeros`:', numeros)
print('Todos los números de la lista `numeros` al cuadrado:', resultado)

resultado = [n**2 for n in numeros]
print('Todos los números de la lista `numeros` al cuadrado:', resultado)

resultado = list(map(lambda n: n ** 2, numeros))
print('Todos los números de la lista `numeros` al cuadrado:', resultado)
