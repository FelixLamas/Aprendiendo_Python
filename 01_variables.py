my_variable = 'mi primer variable'
print(my_variable)
tamanio=len(my_variable)
print(type(my_variable))
print(tamanio)

print('El tamaño de la variable es: ' , tamanio , ' asi de debe contatenar') # Esto funciona porque se usa una coma para separar los argumentos
# print('El tamaño de la variable es: ' + tamanio) # Esto no funciona porque no se puede concatenar un string con un int

#variables en una sola línea
nombre, edad, ciudad = 'Juan', 30, 'Madrid'
print(nombre, edad, ciudad)
print('Hola, soy ' + nombre + ' y tengo ' + str(edad) + ' años y vivo en ' + ciudad)