#dos tipos de datos numericos
#enteros
10
#flotantes
14.4
print(type(9))
print(type(10.2)) #salida:
#<class 'int'>#
#<class 'float'>
#Podemos hacer tipicas operaciones aritmeticas.
r1 = 3+3
r2 = 3 -1
r3 = 3/2
r4 = 4*4
r5 = 1+1.0 #entreo mas flotante = flotante
r6 = 1* 2.0
### Otras operaciones
r7 = 2**3 #elevar a la potencia.
#operador de modulo, cuando quieres el reciduo
r8 = 3//2 #solamente a la parte entera
r9 = 3 % 2 #devuelve el residuo de una operacion
r10 = 10%3 #residuo de una division con el operador de modulo
r11 = 20 - 10 / 5 * 3**2
r12 = (20 - 10) / (5 * 3**2)
#mandamos a imprimir para ver las salidas
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print(r8)
print(r9)
print(r10)
print(r11)
print(r12)
######
#para pedir cosas al usuario
edad = input("Inserte su edad:")
print(edad)
#esta es la salida
#Inserte su edad:23
#23
#pero le sumamos otra cantidad
edad2 = int(edad) + 5
print(edad2)
# da un error pq todo lo que insertamos es un string
# un texto no es un numero
#por lo tanto ponemos un int y se lo pasamos la variable
#ahora si saldria 28 si ingresamos 23
