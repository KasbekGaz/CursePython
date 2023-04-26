#Datos que  no se puede reasignar
#sirve para definir datos inmutables
#sirve para seguridad y para que se ejecuten maas rapido
#x = (1,2,3)
# print(x)
# print(type(x))

#tambien se pueden crear atraves de la funcion tuple()
# y = tuple((3,4,5))
# print(y)

#Para ver que podemos hacer con tupla
# print(dir(x))
#tiene menos metodos porque no podemos cambiarla solo podemos reutilizar metodos

#que pasa sis olo pasamos un dato
#x = (1)
#no sepuede poner asi sino asi
#x = (1,) #sin olvidar la coma

#x = (1,2,3,4,5)
#print(x[0])
#print(x[4])

# x = (1,2,3,4,5)
# del x
# print(x) #no esta definida es el error pero es porque lo elimine anteriormente

#Lo que podemos hacer es un diccionario donde una clave puede ser una tupla

location = {
    (35.123123, 39.00001234) : "Tokyo",
    (20.123124, 123.123124124) : "New York"
}

print(location)
