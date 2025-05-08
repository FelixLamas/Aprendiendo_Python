# cadenas de texto o cadena de caracteres
# print('Hola mundo')
my_string = 'Hola mundo'
print(my_string)
print(type(my_string)) # type() devuelve el tipo de dato de la variable
# print(my_string[0]) # Esto imprime el primer caracter de la cadena
# print(my_string[1]) # Esto imprime el segundo caracter de la cadena
# len(my_string) # Esto devuelve el tamaño de la cadena
# print(my_string[0:4]) # Esto imprime los caracteres de la posición 0 a la 4 (sin incluir la 4)

#concatena strings
print('Hola' + ' ' + 'mundo') # Esto concatena dos cadenas de texto
print('Hola' + ' ' + 'mundo' + ' ' + str(5)) # Esto concatena dos cadenas de texto y un número

print('Hola' * 3) # Esto imprime la cadena 'Hola' 3 veces
print('Hola' * 3 + ' ' + 'mundo') # Esto imprime la cadena 'Hola' 3 veces y luego la cadena 'mundo'
#salto de línea
print('Hola\nmundo') # Esto imprime 'Hola' y luego 'mundo' en la siguiente línea
print('Hola\tmundo') # Esto imprime 'Hola' y luego 'mundo' con un tabulador entre ellos
print('Hola\\mundo') # Esto imprime 'Hola' y luego 'mundo' con una barra invertida entre ellos
print('Hola\'mundo') # Esto imprime 'Hola' y luego 'mundo' con una comilla simple entre ellos
print("Hola\"mundo") # Esto imprime 'Hola' y luego 'mundo' con una comilla doble entre ellos
print('Hola "mundo"') # Esto imprime 'Hola' y luego 'mundo' con una comilla doble entre ellos
#funciones de cadenas de texto
print('Hola'.upper()) # Esto convierte la cadena 'Hola' a mayúsculas
print('Hola'.lower()) # Esto convierte la cadena 'Hola' a minúsculas
print('Hola'.capitalize()) # Esto convierte la cadena 'Hola' a minúsculas y la primera letra a mayúscula
print('Hola'.title()) # Esto convierte la cadena 'Hola' a minúsculas y la primera letra de cada palabra a mayúscula
print('Hola'.swapcase()) # Esto convierte la cadena 'Hola' a mayúsculas y la primera letra a minúsculas
print('Hola'.replace('o', 'a')) # Esto reemplaza la letra 'o' por la letra 'a' en la cadena 'Hola'
print('Hola'.find('o')) # Esto busca la letra 'o' en la cadena 'Hola' y devuelve su posición
print('Hola'.count('o')) # Esto cuenta cuantas veces aparece la letra 'o' en la cadena 'Hola'
print('Hola'.startswith('H')) # Esto verifica si la cadena 'Hola' empieza con la letra 'H'
print('Hola'.endswith('a')) # Esto verifica si la cadena 'Hola' termina con la letra 'a'
print('Hola'.isalpha()) # Esto verifica si la cadena 'Hola' solo contiene letras
print('Hola123'.isalnum()) # Esto verifica si la cadena 'Hola123' solo contiene letras y números
print('Hola123'.isdigit()) # Esto verifica si la cadena 'Hola123' solo contiene números
print('Hola123'.isnumeric()) # Esto verifica si la cadena 'Hola123' solo contiene números
print('Hola123'.isdecimal()) # Esto verifica si la cadena 'Hola123' solo contiene números decimales
print('Hola123'.isspace()) # Esto verifica si la cadena 'Hola123' solo contiene espacios
print('Hola123'.istitle()) # Esto verifica si la cadena 'Hola123' es un título (primera letra de cada palabra en mayúscula)
print('Hola123'.isupper()) # Esto verifica si la cadena 'Hola123' está en mayúsculas
print('Hola123'.islower()) # Esto verifica si la cadena 'Hola123' está en minúsculas
print('Hola123'.isidentifier()) # Esto verifica si la cadena 'Hola123' es un identificador válido (nombre de variable)
print('Hola123'.isprintable()) # Esto verifica si la cadena 'Hola123' es imprimible (no contiene caracteres no imprimibles)
print('Hola123'.isnumeric()) # Esto verifica si la cadena 'Hola123' es numérica (solo contiene números)
print('Hola123'.isdecimal()) # Esto verifica si la cadena 'Hola123' es decimal (solo contiene números decimales)
print('Hola123'.isidentifier()) # Esto verifica si la cadena 'Hola123' es un identificador válido (nombre de variable)
print('Hola123'.isprintable()) # Esto verifica si la cadena 'Hola123' es imprimible (no contiene caracteres no imprimibles)

#formateo de cadenas
print('Hola {}'.format('mundo')) # Esto imprime 'Hola mundo' usando el método format
print('Hola {0}'.format('mundo')) # Esto imprime 'Hola mundo' usando el método format con un índice
print('Hola {0} {1}'.format('mundo', 'mundo')) # Esto imprime 'Hola mundo mundo' usando el método format con dos índices
print('hola %s'.format('mundo')) # Esto imprime 'Hola mundo' usando el método format con un índice
print('Hola %s %s' %('mundo', 'mundo')) # esto imprimo hola mundo usando las variables de formato %s
print('Hola %d' % 5) # Esto imprime 'Hola 5' usando el método format con un número entero
print('Hola %f' % 5.5) # Esto imprime 'Hola 5.5' usando el método format con un número decimal
print('Hola %x' % 5) # Esto imprime 'Hola 5' usando el método format con un número hexadecimal
print('Hola %o' % 5) # Esto imprime 'Hola 5' usando el método format con un número octal
print('Hola %e' % 5.5) # Esto imprime 'Hola 5.5' usando el método format con un número en notación científica
print('Hola %E' % 5.5) # Esto imprime 'Hola 5.5' usando el método format con un número en notación científica

#inferencia de tipos
# Esto significa que el tipo de dato de una variable se infiere automáticamente al asignarle un valor
# Esto es útil porque no tenemos que especificar el tipo de dato de la variable al declararla
# Por ejemplo, si asignamos un número entero a una variable, el tipo de dato de la variable será int
# Si asignamos un número decimal a una variable, el tipo de dato de la variable será float
# Si asignamos una cadena de texto a una variable, el tipo de dato de la variable será str
# Si asignamos una lista a una variable, el tipo de dato de la variable será list
print(f'Hola {my_string}') # Esto imprime 'Hola Hola mundo' usando el método format con una variable
print(f'Hola {my_string} {5}') # Esto imprime 'Hola Hola mundo 5' usando el método format con una variable y un número 

#desempaquetado de cadenas
a, b = 'Hola', 'mundo' # Esto desempaqueta la cadena 'Hola mundo' en dos variables
print(a) # Esto imprime 'Hola'
print(b) # Esto imprime 'mundo'
print(a, b) # Esto imprime 'Hola mundo'
print(f'{a} {b}') # Esto imprime 'Hola mundo' usando el método format con dos variables

#division de cadenas
# Esto significa que podemos dividir una cadena en varias partes usando un separador
# Por ejemplo, si tenemos una cadena 'Hola mundo' y queremos dividirla en dos partes usando el espacio como separador, podemos usar el método split
# Esto nos devolverá una lista con dos elementos: ['Hola', 'mundo']
# También podemos usar el método join para unir una lista de cadenas en una sola cadena usando un separador
my_string = 'Hola mundo'
my_string = my_string[-2]
print(my_string) # Esto imprime 'mundo'
my_string = 'Hola mundo'
my_string = my_string.split(' ') # Esto divide la cadena 'Hola mundo' en dos partes usando el espacio como separador
print(my_string) # Esto imprime ['Hola', 'mundo']
new_string = ' '.join(my_string) # Esto une la lista ['Hola', 'mundo'] en una sola cadena usando el espacio como separador
print(new_string) # Esto imprime 'Hola mundo'