# ============================================================= #
# Ejercicio 6.1: Construir un patrón con el carácter asterisco. #
# ------------------------------------------------------------- #
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# ============================================================= #

for i in range(9):
	if i <= 4:
		for j in range(i + 1):
			print('*', end=' ')
	else:
		for j in range(9 - i):
			print('*', end=' ')
	print('\n')

# ============================================================= #
# Ejercicio 6.2: Capturar una palabra o frase del usuario e     #
# invertirla.                                                   #
# ============================================================= #

frase = input('Escriba una frase o palabra: ')

print('La frase original es:', frase)

# Python => nohtyP

# Solución 1:

frase_invertida = ''

for i in range(len(frase) - 1, -1, -1):
    frase_invertida += frase[i]

print('Frase invertida:', frase_invertida)

# Solución 2:

frase_invertida = frase[::-1]
print('\nFrase invertida:', frase_invertida)

# Ejercicio 6.3: Generar los primeros 50 números de la serie Fibonacci.

a = 0
b = 1

vueltas = 0

while vueltas <= 49:
	vueltas += 1
	c = b + a
	a = b
	b = c
	# a, b = b, a + b
	print(a, end=' ')

# Ejercicio 6.4: Calcular el factorial de un número dado por el usuario.

# Solución:

# 0! = 1
# 1! = 1

# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 6! = 720

numero = int(input('Digite un número entero positivo: '))

if numero >= 0:
    factorial = 1

    if numero == 0 or numero == 1:
        factorial = 1
    else:
        for i in range(1, numero + 1):
            factorial *= i
    
    print(f'{numero}! = {factorial}')
else:
    print('MENSAJE: Ha escrito un valor negativo. La función factorial no está definida para los números negativos.')

# Ejercicio 6.5: Construir un patrón con asteriscos que represente la letra A.

# Ejercicio 6.6: Encontrar todos los números pares que hay en el rango 100 a 400.

# Ejercicio 6.7: Construir un patrón con asteriscos que represente la letra E.

# Ejercicio 6.8: Contar la cantidad de dígitos y letras que tiene un texto.

# Ejercicio 6.9: Construir un patrón con asteriscos que represente la letra Z.

# Ejercicio 6.10: Realizar cálculos de estadísticos básicos: media, mínimo, máximo.

# Ejercicio 9.11: Solicitar al usuario una cantidad arbitria de valor numéricos y luego calcular su suma y productoria.