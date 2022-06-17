# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Introducción a los condicionales  ................       ? #
#		Ejemplo 1. Número Mayor a Otro  ..............       ? #
#		Ejemplo 2. Incremento de Ahorros  ............       ? #
#	Condiciones Múltiples  ...........................       ? #
#	Condiciones Compuestas  ..........................       ? #
# ============================================================ #

# ============================================================ #
#               Introducción a los condicionales               #
# ============================================================ #
#                             `if`                             #
# ============================================================ #

edad = 17

if edad <= 17:
	print('Ud. es menor de edad.\n')
else:
	print('Ud. es mayor de edad.\n')

if edad < 18:
	print('Ud. es menor de edad.\n')
else:
	print('Ud. es mayor de edad.\n')

edad = 29

if edad < 18:
	print('Ud. es menor de edad.\n')
else:
	print('Ud. es mayor de edad.')
	print('Puede entrar a la disco.\n')

# ============================================================ #
#                Ejemplo 1. Número Mayor a Otro                #
# ============================================================ #

n1 = int(input('Ingrese primer numero: '))
n2 = int(input('Ingrese segundo numero: '))

if n1 > n2:
	print('La variable `n1` es mayor que `n2`: {}'.format(n1))

print('El programa ha finalizado.\n')

# ============================================================ #
#               Ejemplo 2. Incremento de Ahorros               #
# ============================================================ #

ahorro = float(input('Escriba la cantidad actual de dinero que tiene en ahorros:'))

if ahorro > 0:
    if ahorro < 1000000:
        ahorro *= 1.10
    elif ahorro < 3000000:
        ahorro *= 1.07
    elif ahorro < 10000000:
        ahorro *= 1.05
    else:
        ahorro *= 1.03
    
    print('El ahorro se ha incremando a {}'.format(ahorro))
else:
    print('Ud. ha digitado una cantidad negativa o igual a cero.')

print('\nEl programa ha finalizado.')

# ============================================================ #
#                    Condiciones Múltiples                     #
# ============================================================ #

numero = int(input('Escriba un número entero: '))

if numero % 5 == 0 and numero >= 20 and numero <= 40:
    print('El número {} es divisible entre 5 y se halla en el rango 20 a 40.'.format(numero))
else:
    print('El número {} no es divisible entre 5 y no se halla en el rango 20 a 40.'.format(numero))

# ============================================================ #
#               Condiciones Múltiples (Mejora)                 #
# ============================================================ #

numero = int(input('Escriba un número entero: '))

# numero >= 20 and numero <= 40
# a <= x <= b

# 20 <= numero <= 40

if numero % 5 == 0 and 20 <= numero <= 40:
    print('\nEl número {} es divisible entre 5 y se halla en el rango 20 a 40.'.format(numero))
else:
    print('\nEl número {} no es divisible entre 5 y no se halla en el rango 20 a 40.'.format(numero))

# ============================================================ #
#                    Condiciones Compuestas                    #
# ============================================================ #

agniosExperiencia = int(input('Escriba la cantidad de años de experiencia programando: '))
lenguaje = input('Escriba el lenguaje de programación que domina: ')

if agniosExperiencia >= 5 or lenguaje in ['Python', 'Java', 'JavaScript']:
    print('Ud. ha calificado para trabajar con nosotros.')
else:
    print('Ud. puede intentar en otra ocasión.')