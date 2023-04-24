#Abreviando string ponemos la variable myStr.
myStr = "Hello World"   #TEXTO PRINCIPAL
#podemos dividirlo obtener caracteres etc.
#usaremos dir() para ver que podemos hacer con cierto tipo de dato.
#print(dir(myStr))
#Aqui se obtienen metodos y con el podemos alterar datos.
#Por ejemplo title que es para poner todas las primeras letras en mayusculas
print(myStr.upper()) #mayusculas
print(myStr.lower()) #todas en minusculas
print(myStr.swapcase()) #las primeras minusculas y las demas mayusculas.
print(myStr.capitalize()) #Mantener las primeras letras en mayusculas
print(myStr.replace('Hello', 'Bye')) #metodo para cambiar una cadena y reemplazarla.
print(myStr.count('l')) #cuantas veces sale un caracter l
print(myStr.count('o')) #cuantas veces sale un caracter o
print(myStr.count(' ')) #cuantas veces sale un caracter vacio
#para saber si esta cadena empieza con algo se usa esto.
print(myStr.startswith('hola'))
#Aqui la salida es un false porque queremos saber si, si o no, empieza con lo que yo le pida.
#Python usa los booleanos es decir false
print(myStr.startswith('Hello')) #si ahora usamos esto nos dara en true que es verdadero
#Hay que tener cuenta que si la palabra esta mal escrita como por ejemplo no tomamos en cuenta las mayusculas
#lo tomara como falso pq no es igual a las mismas caracteres que buscamos.
#El metodo contrario
print(myStr.endswith('World')) #verdadero
#Dividir en dos variables o en dos datos.
#Divide la cadena con el metodo split
##print(myStr.split())
#funciona pero tomando en cuenta el espacio.
# es decir sale asi= ['Hello', 'World'] pero le podemos decir que por una coma.
#print(myStr.split(','))
#Modificamos el texto principal
#la salida es = ['Hello', 'World'] lo cual es lo mismo
#podemos separa apartir de un caracter
print(myStr.split('o')) #la o por ejemplo
# la salida es una lista = ['Hell', ',W', 'rld']
#DATO: la lista sirve para ordenar ciertos tipos de datos.
#Con ello tambien podemos buscar caracteres
print(myStr.find('o')) #vamos a buscar donde esta la o
#salida = 4
#Si buscamos la coma seria el indice 5
#Se cuenta desde 0 -> en adelante
#tambien cuenta espacios
#Como saber cuanto mide esta vairable
print(len(myStr)) #salida = 11 en efecto eso es aqui si cuenta desde uno
print(myStr.isnumeric) #para ver si es numerico
print(myStr.isalpha) #si el alfanumerico

print(myStr[4]) #cuando queremos la pocision de nuestra cadena de caracteres.
print(myStr[0]) #la salida de antes es o y en esta es H por la
#Posision que tienen nuestros caracteres.

#en orden inverso
print(myStr[-1]) # este seria d
##################
#CONCATENAR
nombre = 'oswaldo'
print('Mi nombre es ' + nombre)
#otra forma de pasar la variable e imprimirla. no olvides la f
#y entre llaves
print(f'Mi nombre es {nombre}')
#usando format, le pasamos la posicion 0 en lugar de la variable
#en el metodo format es donde va la vairable.
print("Mi nombre es {0}".format(nombre))

