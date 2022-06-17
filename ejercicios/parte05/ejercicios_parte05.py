from random import randint

# ============================================================ #
# Ejercicio 5.1. Capturar la temperatura (sea en grados        #
# Celcius o Fahrenheit) y convertirla a la escala contraria.   #
# ============================================================ #

# captura = input('Escriba la temperatura actual en su región (e.g., 100°C, 32°F)\n> ')

def captureTemperature(cpt):
	if cpt[-2:] == '°C':
		convertToFahrenheit = (float(cpt[:-2]) * 9/5) + 32
		return convertToFahrenheit
	elif cpt[-2:] == '°F':
		convertToCelcius = (float(cpt[:-2]) - 32) * 5/9
		return convertToCelcius
	else:
		return 'No ha escrito los valores de temperaturas adecuadamente.'

# a = captureTemperature(captura)

# print(a)

# ============================================================ #
# Ejercicio 5.2. Pedir al usuario que adivine un número.       #
# Sólo un intento.                                             #
# ============================================================ #

# print('Adivine un número del 1 al 10')

# numero = int(input('Ingrese un número: '))

def guessNumber(n):
	numeroAleatorio = randint(1, 10)
	if n == numeroAleatorio:
		return 'Has ganado! Muy bien!'
	else:
		return 'No has adivinado el número al primer intento.\nEl número era: %i.' % numeroAleatorio

# b = guessNumber(numero)

# print(b)

# ============================================================ #
# Ejercicio 5.3. Comprobar el producto de mayor precio         #
# entre tres productos.										   #
# ============================================================ #

precio1 = float(input('Escriba el precio del primer producto: '))
precio2 = float(input('Escriba el precio del segundo producto: '))
precio3 = float(input('Escriba el precio del tercer producto: '))

def mostExpensiveProduct(p1, p2, p3):
	if p1 > p2 and p1 > p3:
		return 'El producto más costoso es %f' % p1
	elif p2 > p1 and p2 > p3:
		return 'El producto más costoso es %f' % p2
	elif p3 > p1 and p3 > p2:
		return 'El producto más costoso es %f' % p3
	else:
		return 'Los tres productos cuestan lo mismo.'

c = mostExpensiveProduct(precio1, precio2, precio3)

print(c)

# ============================================================ #
# Ejercicio 5.4. Dada la recta y = 6x + 10, comprobar si
# un punto dado pertenece a ella.
# ============================================================ #

x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))

valor = 6 * x + 10

if valor == y:
	print('El punto ({}, {}) se halla en la recta y = 6x + 10'.format(x, y))
else:
	print('El punto ({}, {}) no se halla en la recta y = 6x + 10'.format(x, y))

# ============================================================ #
# Ejercicio 5.5. Dadas las rectas y = 2x - 2, y = x + 1,
# x = 10 comprobar si un punto está en el área comprendida
# entre las rectas.
# ============================================================ #

x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))

if x <= 10:
	valor_1 = 2 * x - 2
	valor_2 = x + 1

	if valor_2 <= y <= valor_1:
		print('El punto ({}, {}) se halla en el área de las tres rectas.'.format(x, y))
	else:
		print('El punto ({}, {}) no se halla en el área de las tres rectas.'.format(x, y))
else:
	print('El punto ({}, {}) no se halla en el área de las tres rectas.'.format(x, y))

# ============================================================ #
# Ejercicio 5.6. Aplicar descuento según la cantidad
# de productos comprados. Cada producto cuesta $100.000.
# ============================================================ #

cantidad = int(input('Digite la cantidad de productos comprados: '))

if cantidad > 0:
    total = cantidad * 100000

    if 5 <= cantidad <= 20:
        total *= 0.99
    elif 20 < cantidad <= 50:
        total *= 0.97
    elif 50 < cantidad <= 100:
        total *= 0.93
    elif cantidad > 100:
        total *= 0.90

    print('El total a pagar es igual a ${}'.format(total))
else:
    print('Ha digitado una cantidad inválida.')

# ============================================================ #
# Ejercicio 5.7. Categorizar según la cantidad de puntos       #
# obtenidos por un jugador.									   #
# ============================================================ #
#  ____________________________                                #
# | **Puntos** | **Categoría** |							   #
# |------------|---------------|							   #
# | 0-100      | Principiante  |							   #
# | 101-500    | Estándar      |							   #
# | 501-2000   | Experimentado |							   #
# | 2000>      | Máster        |							   #
# ============================================================ #

puntos = int(input('Digite la cantidad de puntos obtenidos: '))

categoria = None

if puntos <= 100:
    categoria = 'Principiante'
elif puntos <= 500:
    categoria = 'Estándar'
elif puntos <= 2000:
    categoria = 'Experimentado'
else:
    categoria = 'Máster'

print('La categoría del jugador es %s' % categoria)

# ============================================================ #
# Ejercicio 5.8. Determinar si un número dado por el
# usuario es par o impar.
# ============================================================ #

n_par_impar = float(input('Ingrese un número (ya sea par o impar): '))

if n_par_impar % 2 == 0:
	print('es par')
else:
	print('no es par')

# ============================================================ #
# Ejercicio 5.9. Comprobar si un número es capicúa.
# ============================================================ #

numero = int(input('Digite un número entero positivo: '))

if numero >= 0:
    
    if str(numero) == str(numero)[::-1]:
        print('%i es capicúa.' % numero)
    else:
        print('%i no es capicúa.' % numero)

else:
    print('El número debe ser positivo.')

# ============================================================ #
# Ejercicio 5.10. Validar si tres valores numéricos
# pueden pertenecer al esquema de colores RGB.
# ============================================================ #

rojo = int(input('Digite la cantidad de color rojo (0 - 255): '))
verde = int(input('Digite la cantidad de color verde (0 - 255): '))
azul = int(input('Digite la cantidad de color azul (0 - 255): '))

if 0 <= rojo <= 255 and 0 <= verde <= 255 and 0 <= azul <= 255:
    print('Los valores %i %i %i corresponden para el esquema RGB.' % (rojo, verde, azul))
else:
    print('Los valores %i %i %i NO corresponden para el esquema RGB.' % (rojo, verde, azul))