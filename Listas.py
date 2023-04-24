# esto es una lista [1, 'hola'and, 1.14, true]
listademo = [1, 'hola', 1.14, True, [1,2,3,5]]
colores = ['rojo', 'verde', 'morado']
#solo acepta 1 argumento
#usamos una tupla
n_numeros = list((1,2,3,4,5))
print(n_numeros)
print(type(n_numeros))

#rangos (valor inicial,valor final)
#lo pasamos a lista
#rango = list(range(1, 101))
#print(rango)

#Obtener informacion de una lista
print(type(colores))
##metodos que puedo usar con list
#print(dir(colores)) #saber que puedo ejecutar
# print(len(colores))
# print(colores[1])
# print(colores[0])
# para saber si algo esta en la lista
print('verde' in colores)
#si el modulo esta entonces es True
print('Moco' in colores)
#esto pues es False
