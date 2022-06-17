# ============================================================ #
# Multiply: Este código no se ejecuta correctamente. Intenta   #
# averiguar por qué.                                           #
# ============================================================ #

def multiply(a, b):
	mul = a * b
	return mul

a = multiply(2, 2)

# print(a)

# ============================================================ #
# Sum Arrays: Escribe una función que tome una matriz de       #
# números y devuelva la suma de los mismos. Los números        #
# pueden ser negativos o no enteros. Si el array no            #
# contiene ningún número entonces debe devolver 0.             #
# ============================================================ #

def sum_array(a):
	return sum(a)
	
b = sum_array([1, 5.2, 4, 0, -1])

# print(b)

# ============================================================ #
# Returning Strings: Haz una función que devuelva una          #
# declaración de saludo que utilice una entrada; tu            #
# programa debería devolver, "Hola, <nombre> ¿cómo estás       #
# hoy?".                                                       #
# [Asegúrate de escribir exactamente lo que escribí o el       #
# programa podría no ejecutarse correctamente].                #
# ============================================================ #

def greet(name):
	#Good Luck (like you need it)
	return f'Hello, {name} how are you doing today?'

c = greet('Cesar')

# print(c)

# ============================================================ #
# Remove First and Last Character: Es bastante sencillo.       #
# Tu objetivo es crear una función que elimine el primer       #
# y el último carácter de una cadena. Se le da un parámetro,   #
# la cadena original. No tienes que preocuparte por las        #
# cadenas con menos de dos caracteres.                         #
# ============================================================ #

def remove_char(s):
	#your code here
	return s[1:-1]

d = remove_char('Hola')

# print(d)

# ============================================================ #
# Convert a Number to a String!: Necesitamos una función       #
# que pueda transformar un número en una cadena.               #
# ¿Qué formas de conseguirlo conoces?                          #
# ============================================================ #

def number_to_string(num):
	# Return a string of the number here!
	return str(num)

e = number_to_string(4)

# print(e)

# ============================================================ #
# Convert number to reversed array of digits: Dado un número   #
# aleatorio no negativo, hay que devolver los dígitos de       #
# este número dentro de una matriz en orden inverso.           #
# ============================================================ #

def digitize(n):
	stringToList = str(n)[::-1]
	listInverted = [int(n) for n in stringToList]
	return listInverted

f = digitize(34356467)

# print(f)

# ============================================================ #
# Beginner Series #1 School Paperwork: Tus compañeros te       #
# han pedido que les copies unos papeles. Sabes que hay        #
# "n" compañeros y que la documentación tiene "m" páginas.     #
# Tu tarea es calcular cuántas páginas en blanco necesitas.    #
# Si n < 0 o m < 0 devuelve 0.                                 #
# ============================================================ #

def paperwork(n, m):
	# Happy Coding! ^_^
	if n < 0 or m < 0:
		return 0
	else:
		quantinty = n * m
		return quantinty

f = paperwork(21, 54)

# print(f)

# ============================================================ #
# Function 1 - hello world: Haz una función sencilla llamada   #
# greet que devuelva el famosísimo "¡hola mundo!".             #
# ============================================================ #

def helloWorld():
    return "hello world!"

g = helloWorld()

# print(g)

# ============================================================ #
# Beginner - Lost Without a Map: Dado un array de enteros,     #
# devuelve un nuevo array con cada valor duplicado.            #
# ============================================================ #

def maps(numeros):
    listNumber = [ numeros[i] * 2 for i in range(len(numeros)) ]
    return listNumber

h = maps([1, 2, 3])

# print(h)

# ============================================================ #
# Añade el valor "codewars" a la matriz de sitios web.         #
# Después de que su código se ejecute la matriz                #
# de sitios web debe == ["codewars"]                           #
# ============================================================ #

websites = []

websites.append('codewars')

print(websites)