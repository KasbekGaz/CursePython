#Tipos de datos en Python

#### String
print("Hello world")
print('hello world')
print(''' hello world''')
#Las mandamos amiprimir con la funcion  print
#esto segun es para ver el tipo de dato que pasamos
#para ver realmente en e interprete debemos pasarla a la funcion print:
print(type('helloworld'))
#concatenar:
print("bye" + "worlds")#para concatenar
x = 3 + 4  #para sumar
# 3 + 4 = x asi no jala
print (x)

#### Numeros
# integer
print(type(30)) #para ver el tipo de dato #entero
# float
print(type(30.5)) #decimal
#boolean tipo de dato logico
print(type(True))
print(type(False))
# Lists
[10, 20, 30, 40, 50]
['saludos', 'hola conschtumare']
[10, 'hello', 10.2]
[] #lista vacia
print(type(['elemento',12]))
# Tuplas similar a las listas pero no se pueden cambiar los datos.
(10, 20, 30, 55)
()#tupla vacia
print(type((10, 20, 30)))
# diccionarios: agrupar distintos datos de la misma entidad
#siempre como CLAVE:VALOR
{     #ejemplo de una entidad PERSONA
	 "nombre":"Ryan",
	"apellido1":"papadopolus",
	"apellido2":"eterminator",
}
# Aqui nos marca un error de algo equisde pero no se de que
#print(type({"pais": "mexico", "latitud": 123.123.123, "longitud": 123.456.78.9}))
#Tipos de datos que no estan definidos
None
print(type(None))
### Variables
name = "Oswaldo" #creamos una variable llamada name
#del cual guardamos el string "oswaldo"
print(10 + 101) #podemos guardar el dato de la suma
print(name) #y aqui la mandamos a pantalla
## Que tipo de datos puedo poner
x = 1000
book = "digital fortress" # Son variables distintas
Book = "dgitital conchetumar" #case sensitivie
#porque una empieza con b y el otro con B
# no se debe de empezar con un numero
# 2book # Efectivamente no se puede
#con guion bajo si pero no con guion normal
#asd-a =1
otro_dato = 0
# Podemos almacenar varios datos ye imprimirlos en una sola linea
x, book = 100, "El libro de san ciprano"
print(x, book)
# convenciones.
bookName = "libro1"  #camel case
book_name = "libro2" # snake case
Book_Name = "libro3" # Pasacl case
print(bookName, book_name, Book_Name)
#valores que no cambian
#como PI
pi = 3.1416 #CONSTANTE
#Valores que no cambien en mayusculas
PI = 3.1416
MY_NAME = "Oswaldo"
# Lenguaje dinamico
#Si nuestro variable tiene un string y queremos pasarle otro dato
#no es necesaria transformarla solo con guardarla en la variable 
#ya estaria
book_name = "Yo ROBOT"
#cambiamos el tipo de dato
book_name = 12345
