# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Introducción a las Excepciones  ..................       ? #
#		Captura Segura de un Número Entero  ..........       ? #
#	Excepciones Aritméticas  .........................       ? #
#	Acceso a Elementos de una Lista  .................       ? #
#		Acceso a Índices Negativos  ..................       ? #
#	Diccionarios  ....................................       ? #
#		Uso del Método `get()`  ......................       ? #
#	Atributo de Clase Inexistente  ...................       ? #
#	Acceder a Archivo Inexistente  ...................       ? #
#	Excepción Personalizada  .........................       ? #
# ============================================================ #

# ============================================================ #
#                Introducción a las Excepciones                #
# ============================================================ #

try:
    numero = int(input('Escriba un número entero: '))

    print('Contenido de la variable `numero`:', numero)
    print('El tipo de dato de la variable `numero` es:', type(numero))
except ValueError as e:
    print('ERROR: ', e)

print('\nEl programa ha terminado')

# ============================================================ #
#              Captura Segura de un Número Entero              #
# ============================================================ #

while True:
    try:
        edad = int(input('Escribe su edad: '))

        if edad > 0:
            if edad <= 70:
                break
            else:
                print('MENSAJE: La edad no debe superar los 70 años.')
        else:
            print('MENSAJE: El valor para la edad debe ser un número positivo.')
    except:
        print('MENSAJE: No ha escrito un valor válido. Intente de nuevo.')

print('\nSu edad es:', edad, 'años.')

# ============================================================ #
#                   Excepciones Aritméticas                    #
# ============================================================ #

while True:
    try:
        dividendo = float(input('Escriba el dividendo: '))

        break
    except:
        print('MENSAJE: Debe escribir un valor válido. Intente de nuevo.')

while True:
    try:
        divisor = float(input('Escriba el divisor: '))

        break
    except:
        print('MENSAJE: Debe escribir un valor válido. Intente de nuevo.')

try:
    division = dividendo / divisor

    print('El resultado de la división es:', division)
except ZeroDivisionError as e:
    print('ERROR:', e)
    print('MENSAJE: Intento de división entre cero.')

# ============================================================ #
#               Acceso a Elementos de una Lista                #
# ============================================================ #

lenguajes = ['Python', 'C++', 'JavaScript', 'C#', 'Java', 'C']

print('Cantidad de elementos de la lista `lenguajes`:', len(lenguajes))

print('Primer elemento de la lista `lenguajes`:', lenguajes[0])

indice = 6

try:
    print('Último elemento de la lista `lenguajes`:', lenguajes[indice])
except IndexError:
    print('El índice %i no existe en la lista `lenguajes`' % indice)

# print('El programa ha finalizado.')

print()

# ============================================================ #
#                  Acceso a Índices Negativos                  #
# ============================================================ #

print('Último elemento de la lista `lenguajes`:', lenguajes[-1])

indice = -7

try:
    lenguaje = lenguajes[indice]

    print('Primer elemento de la lista `lenguajes`:', lenguaje)
except:
    print('El índice {} no existe en la lista `lenguajes`.'.format(indice))

print('\nEl programa Python ha terminado.')

# ============================================================ #
#                         Diccionarios                         #
# ============================================================ #

versiones = {'Python': '3.8.1', 'Java': '12', 'JavaScript': 'ES6', 'C#': '8'}

lenguaje = input('Escriba un nombre de lenguaje de programación: ')

try:
    version = versiones[lenguaje]

    print('La versión de {} es {}'.format(lenguaje, version))
except KeyError as e:
    print('ERROR:', e)

print('Fin del programa.')

# ============================================================ #
#                    Uso del Método `get()`                    #
# ============================================================ #

version = versiones.get('java', '1.0.0')
print('\nLa versión de {} es {}'.format('java', version))

# ============================================================ #
#                Atributo de Clase Inexistente                 #
# ============================================================ #

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


computador = Producto(1001, 'Computador', 799)

print('Código:', computador.codigo)
print('Nombre:', computador.nombre)
print('Precio:', computador.precio)

try:
    print('Cantidad:', computador.cantidad)
except AttributeError as e:
    print('Se está tratando de acceder a una propiedad/atributo inexistente')
    print('ERROR:', e)

# ============================================================ #
#                Acceder a Archivo Inexistente                 #
# ============================================================ #

nombre_archivo = 'python.txt'

try:
    with open(nombre_archivo, 'r') as f:
        for l in f.readlines():
            print(l)
except FileNotFoundError as e:
    print('ERROR:', e)

# ============================================================ #
#                   Excepción Personalizada                    #
# ============================================================ #

class ValorMinimoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return 'ValorMinimoError: {}'.format(self.message)
        else:
            return 'Se ha generado el error ValorMinimoError.'

class ValorMaximoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return 'ValorMaximoError: {}'.format(self.message)
        else:
            return 'Se ha generado el error ValorMaximoError.'


minimo = 10
maximo = 20

while True:
    try:
        numero = int(input('Escriba un número entre {} y {}: '.format(minimo, maximo)))

        if numero < minimo:
            raise ValorMinimoError('Ha escrito un valor menor a {}.'.format(minimo))
        elif numero > maximo:
            raise ValorMaximoError('Ha escrito un valor mayor a {}.'.format(maximo))
        
        print('Ha escrito un entre {} y {}.'.format(minimo, maximo))

        break
    except ValueError:
        print('Debe escribir un valor entero válido.')
    except ValorMinimoError as e:
        print('ERROR:', e)
    except ValorMaximoError as e:
        print('ERROR:', e)