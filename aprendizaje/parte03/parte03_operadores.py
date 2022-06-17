# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Operadores Numéricos  ............................       ? #
#	Operadores de Comparación  .......................       ? #
#	Operadores Lógicos  ..............................       ? #
#	Operadores a Nivel de Bits  ......................       ? #
#	Operadores de Asignación  ........................       ? #
#	Precedencia (Jerarquía) de Operadores  ...........       ? #
#	Expresiones Algebraicas a Programáticas  .........       ? #
#		Ejemplo 1  ...................................       ? #
#		Ejemplo 2  ...................................       ? #
#		Ejemplo 3  ...................................       ? #
#		Ejemplo 4  ...................................       ? #
#		Ejemplo 5  ...................................       ? #
# ============================================================ #

from math import pi, sqrt

# ============================================================ #
#                     Operadores Numéricos                     #
# ============================================================ #
#                              +                               #
# ============================================================ #

numero_1 = 2
numero_2 = 3

suma = numero_1 + numero_2
print(f'La suma de {numero_1} y {numero_2} es igual a {suma}')

# ============================================================ #
#                              -                               #
# ============================================================ #

numero_1 = 5
numero_2 = 3

resta = numero_1 - numero_2

print(f'La resta de {numero_1} y {numero_2} es igual {resta}.')

numero = 100
print('\nEl valor de la variable `numero` es igual a', -numero)
print('El valor de la variable `numero` es igual a', numero)

numero = -100
print('\nEl valor de la variable `numero` es igual a', numero)
print('El valor de la variable `numero` es igual a', -numero)

print('\nEl valor de la variable `pi` es igual a', pi)
print('El valor de la variable `pi` es igual a', -pi)

# ============================================================ #
#                              *                               #
# ============================================================ #

numero_1 = 3
numero_2 = 7

producto = numero_1 * numero_2
print(f'El producto de {numero_1} por {numero_2} es igual a {producto}.')

# ============================================================ #
#                              /                               #
# ============================================================ #

numero_1 = 1
numero_2 = 2

division = numero_1 / numero_2
print('La división de {} entre {} es igual a {}.'.format(numero_1, numero_2, division))

# ============================================================ #
#                      División Entre Cero                     #
# ============================================================ #

numero_1 = 5
numero_2 = 0

print('Solución #1:')

if numero_2 != 0:
    division = numero_1 / numero_2
    print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))
else:
    print('MENSAJE: La división entre cero no está permitida.')

print('\nSolución #2:')

try:
    division = numero_1 / numero_2
    print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))
except ZeroDivisionError as e:
    print('Error:', e)

# ============================================================ #
#                              //                              #
# ============================================================ #

numero_1 = 5
numero_2 = 2

division = numero_1 / numero_2

print(f'División entre {numero_1} y {numero_2} es igual a {division}.')

division_entero = numero_1 // numero_2
print(f'\nDivisión entera entre {numero_1} y {numero_2} es igual a {division_entero}.')

# ============================================================ #
#                              **                              #
# ============================================================ #

base = 2
exponente = 3

potencia = base ** exponente

print(f'La potencia de {base}^{exponente} es igual a {potencia}.')

potencia = pow(base, exponente)
print(f'\nLa potencia de {base}^{exponente} es igual a {potencia}.')

# ============================================================ #
#                   Operadores de Comparación                  #
# ============================================================ #
#                       == / is / is not                       #
# ============================================================ #

programa_1 = 'Visual Studio Code'
programa_2 = 'Visual Studio Code'
programa_3 = 'isual tudio Code'
programa_4 = 'Visual Studio Code'

igual = programa_1 == programa_2
mismoObjeto = programa_1 is programa_2
distintoObjeto = programa_3 is not programa_4

print("¿'{}' es igual a '{}'?: {}".format(programa_1, programa_2, igual))
print("¿'{}' es igual a '{}'?: {}".format(programa_1, programa_2, mismoObjeto))
print("¿'{}' es distinto a '{}'?: {}".format(programa_1, programa_2, distintoObjeto))

# ============================================================ #
#                             !=                               #
# ============================================================ #

numero_1 = 5
numero_2 = 7

distinto = numero_1 != numero_2

print(f'¿{numero_1} es diferente de {numero_2}?: {distinto}.')

# ============================================================ #
#                             >                                #
# ============================================================ #

numero_1 = 5
numero_2 = 3

mayorQue = numero_1 > numero_2
print('¿{} es mayor que {}?: {}'.format(numero_1, numero_2, mayorQue))

# ============================================================ #
#                             >=                               #
# ============================================================ #

numero_1 = 5
numero_2 = 5

mayorIgualQue = numero_1 >= numero_2
print(f'¿{numero_1} es mayor o igual que {numero_2}?: {mayorIgualQue}')

# ============================================================ #
#                             <                                #
# ============================================================ #

numero_1 = 3
numero_2 = 5

menorQue = numero_1 < numero_2
print('¿{} es menor que {}?: {}'.format(numero_1, numero_2, menorQue))

# ============================================================ #
#                             <=                               #
# ============================================================ #

numero_1 = 3
numero_2 = 3

menorIgualQue = numero_1 <= numero_2
print(f'¿{numero_1} es menor o igual que {numero_2}?: {menorIgualQue}')

# ============================================================ #
#                             and                              #
# ============================================================ #

edad = 19
nombre = 'Daniela'

resultado = edad >= 18 and nombre == 'Daniela'
print('¿La persona se llama Daniela y es mayor de edad?: {}'.format(resultado))

# ============================================================ #
#                              or                              #
# ============================================================ #

edad = 23
profesion = 'Programador'

califica = edad > 20 or profesion == 'Programador'
print('¿La persona tiene más de 20 años o es programadora?:', califica)

# ============================================================ #
#                             not                              #
# ============================================================ #

llueve = True

print('Contenido de la variable `llueve`:', llueve)

llueve = not llueve
print('Contenido de la variable `llueve`:', llueve)

edad = 17
resultado = not edad < 18
print('\nResultado:', resultado)

# ============================================================ #
#                  Operadores a Nivel de Bits                  #
# ============================================================ #
#                           & / and                            #
# ============================================================ #

numero_1 = 5 # 101
numero_2 = 2 # 10

# 101
# 010 &
# ====
# 000

resultado = numero_1 & numero_2

print('numero_1 & numero_2 =', resultado)

# ============================================================ #
#                            | / or                            #
# ============================================================ #

numero_1 = 5 # 101
numero_2 = 2 # 10

# 101
# 010 |
# === 
# 111

# 111 [2] = 7 [10]

resultado = numero_1 | numero_2

print('numero_1 | numero_2 =', resultado)

# ============================================================ #
#                           ~ / not                            #
# ============================================================ #

numero = 5 # 101

# 101 ~
# ===
# -(101 + 1)
# -(110)
# -(6)
# -6

resultado = ~numero

print('~numero =', resultado)

# ============================================================ #
#                           ^ / xor                            #
# ============================================================ #

numero_1 = 5 # 101
numero_2 = 2 # 10

# 101
# 010 ^
# ===
# 111 [2] = 7 [10]

resultado = numero_1 ^ numero_2

print('numero_1 ^ numero_2 =', resultado)

# ============================================================ #
#               Desplazamiento a la Derecha: >>                #
# ============================================================ #

numero = 10 # 1010

# 1010 >> 1 = 0101

resultado = numero >> 1
print('numero >> 1 =', resultado)

# ============================================================ #
#              Desplazamiento a la Izquierda: <<               #
# ============================================================ #

numero = 10 # 1010

# 1010 << 1 = 10100

# 2 ^ 4 + 2 ^ 2 = 16 + 4 = 20

resultado = numero << 1
print('numero << 1 =', resultado)

# ============================================================ #
#                   Operadores de Asignación                   #
# ============================================================ #
#                              =                               #
# ============================================================ #

numero = 10

print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             +=                               #
# ============================================================ #

numero += 90
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             -=                               #
# ============================================================ #

numero -= 80
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             *=                               #
# ============================================================ #

# numero = numero * 5
numero *= 5
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             /=                               #
# ============================================================ #

# numero = numero / 25
numero /= 25
print('Contenido de la variable `numero`:', numero)

numero = round(numero)

# ============================================================ #
#                            //=                               #
# ============================================================ #

numero = numero // 2
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             %=                               #
# ============================================================ #

numero = 10

numero %= 7
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             &=                               #
# ============================================================ #

print('Operador de asignación con and (bitwise): &=')

numero = 5

numero &= 2
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             |=                               #
# ============================================================ #

print('\nOperador de asignación con or (bitwise): |=')

numero = 5

numero |= 2
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#                             ^=                               #
# ============================================================ #
print('\nOperador de asignación con xor (bitwise): ^=')

numero = 5

numero ^= 2
print('Contenido de la variable `numero`:', numero)


# ============================================================ #
#                       >>= / <<=                              #
# ============================================================ #
print('\nOperador de asignación con desplazamiento a la derecha (bitwise): >>=')

numero = 10

numero >>= 1
print('Contenido de la variable `numero`:', numero)

print('\nOperador de asignación con desplazamiento a la izquierda (bitwise): <<=')

numero = 10

numero <<= 1
print('Contenido de la variable `numero`:', numero)

# ============================================================ #
#            Precedencia (Jerarquía) de Operadores             #
# ============================================================ #

resultado = 5/2 + 4
print('El contenido de la variable `resultado` es:', resultado)

resultado = 4 + 5/2
print('\nEl contenido de la variable `resultado` es:', resultado)

resultado = 5/(2 + 4)
print('\nEl contenido de la variable `resultado` es:', resultado)

resultado = 5/(2 + 4) + sqrt(25)
print('\nEl contenido de la variable `resultado` es:', resultado)

resultado = 25 ** 1 / 2
print('\nEl contenido de la variable `resultado` es:', resultado)

resultado = 25 ** (1 / 2)
print('\nEl contenido de la variable `resultado` es:', resultado)

resultado = (13 + 3) ** (1 / 2)
print('\nEl contenido de la variable `resultado` es:', resultado)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = sum(numeros[0:5])
print('\nEl contenido de la variable `resultado` es:', resultado)

numero = -100

resultado = -100 ** (1/2)
print('\nEl contenido de la variable `resultado` es:', resultado)

resultado = -numero ** (1/2)
print('\nEl contenido de la variable `resultado` es:', resultado)
print('Tipo de dato de la variable `resultado`:', type(resultado).__name__)

resultado = (-numero) ** (1/2)
print('\nEl contenido de la variable `resultado` es:', resultado)
print('Tipo de dato de la variable `resultado`:', type(resultado).__name__)

# ============================================================ #
#           Expresiones Algebraicas a Programáticas            #
# ============================================================ #

# ============================================================ #
#          Ejemplo 1. Linealizar ecuación cuadrática.          #
# ============================================================ #

a = 1
b = 0
c = -1

x_1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
x_2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print('Solución 1 (x_1):', x_1)
print('Solución 1 (x_2):', x_2)

# ============================================================ #
#                     Ejemplo 2. X^2 + 4YZ                     #
# ============================================================ #

# 

x = 1
y = 2
z = 3

resultado = x**2 + 4*y*z
print('\nResultado:', resultado)

# ============================================================ #
#                          Ejemplo 3.                          #
# ============================================================ # 

resultado = (x + y)/z + 3*x/5 + 4*y
print('\nResultado:', resultado)

# ============================================================ #
#                          Ejemplo 4.                          #
# ============================================================ # 

c = 5
d = 3

resultado = (4*x**2 - 2*x + 8) / (c - d)
print('\nResultado:', resultado)

# ============================================================ #
#                          Ejemplo 5.                          #
# ============================================================ # 

resultado = 4/3 * math.pi
print('\nResultado:', resultado)