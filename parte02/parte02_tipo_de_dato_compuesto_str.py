# ============================================================ #
#							  ÍNDICE						   #
# ------------------------------------------------------------ #
#	Tipo de Dato str  ................................      15 #
#	    Construcción de una Cadena de Caracteres  ....   29-53 #
#	        Interpolación  ...........................      37 #
#	        `format()`  ..............................      44 #
#	        Formateo con % o Módulo  .................      51 #
#	    Concepto de Inmutabilidad 1/2  ...............      59 #
#	    Concepto de Inmutabilidad 2/2  ...............      77 #
#	    Operaciones Básicas  .........................      86 #
#   Métodos Personalizados versus Integrados  ........     103 #
# ============================================================ #

# ============================================================ #
#                       Tipo de Dato str                       #
# ============================================================ #

nombre = 'Cesar Ojeda'
email = "cesar@mail.co"
direccion = '''Carrera 1 # 13A-29
Aragua - Venezuela
GMT-05
'''

print('Tipo de dato `nombre`:', type(nombre).__name__)
print('Su nombre es:', nombre)

# ============================================================ #
#           Construcción de una Cadena de Caracteres           #
# ============================================================ #

mensaje = 'Bienvenido(a), ' + nombre + '. Correo: ' + email
print('El tipo de dato de la variable `mensaje` es:', type(mensaje))
print(mensaje, '\n')

# ============================================================ #
#                         Interpolación                        #
# ============================================================ #
print('Interpolación:\n')
mensaje = f'Bienvenido(a), {nombre}. Correo: {email}'
print(mensaje, '\n')

# ============================================================ #
#                          `format()`                          #
# ============================================================ #
print('format() de la clase str:\n')
mensaje = 'Bienvenido(a), {}. Correo: {}'.format(nombre, email)
print(mensaje, '\n')

# ============================================================ #
#                    Formateo con % o Módulo                   #
# ============================================================ #

print('Formato con %:\n')
mensaje = 'Bienvenido(a), %s. Correo: %s' % (nombre, email)
print(mensaje)

# ============================================================ #
#                 Concepto de Inmutabilidad 1/2                #
# ============================================================ #

lenguaje = "Python"
print(f'Lenguaje de programación: {lenguaje}\n')
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5], '\n')

# lenguaje[0] = 'p' # TypeError

lenguaje = 'p' + lenguaje[1:]
print(f'Lenguaje de programación: {lenguaje}\n')

# ============================================================ #
#                 Concepto de Inmutabilidad 2/2                #
# ============================================================ #

print(id('python') == id('python'))

lenguaje = 'Python'.lower()
print(f'Lenguaje de programación: {lenguaje}')

# ============================================================ #
#                      Operaciones Básicas                     #
# ============================================================ #

valores = '2,3,5,7,11'
numeros = valores.split(',')
print('Contenido `numeros`:',numeros)

indice = valores.find('2')
print('El índice del elemento "2" es igual a', indice)

indice = valores.find('1')
print('El índice del elemento "1" es igual a', indice)

indice = valores.find('8')
print('El índice del elemento "8" es igual a', indice)

# ============================================================ #
#           Métodos Personalizados versus Integrados           #
# ============================================================ #

def encontrar(cadena, caracter):
    indice = -1
    for i in range(0, len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    return indice

indice = encontrar(valores, '2')
print('El índice del elemento "2" es igual a', indice, '\n')

indice = encontrar(valores, '8')
print('El índice del elemento "8" es igual a', indice)
