#Los sets son utilizados para definir una coleccion que no tiene un indice.
#Por ejemplo el siguiente
colores = {'rojo', 'verde', 'amarillo'}
print(type(colores))
print('rojo' in colores) #tambien podemos ver si existen dentro de una coleccion
#tambien puedo agregar
colores.add('violeta') #asi lo agrega al inicio
print(colores)
colores.remove('verde')
print(colores)
#tambien podemos limpiar
colores.clear()
print(colores)
#salida:
# {'rojo', 'amarillo', 'violeta', 'verde'}
# {'rojo', 'amarillo', 'violeta'}
# set()

#tambien se peude hacer asi
# del colores
# print(colores)

#Se usa como para almacenar conjuntos de datos que no se ordenan
