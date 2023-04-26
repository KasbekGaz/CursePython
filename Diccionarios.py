#cOMO USARLOS suponiendo que tenemos una tienda:
#carrito = [
#    ["libro", 3, 4.99],
#]
#se uede hacer asi pero si tengo mas variables y no solo 1 datos sino cientos.
#seria muy dificil tratar tantos datos
#lO podemos hacer asi

producto ={

    "nombre": "libro",
    "cantidad": 3,
    "precio": 4.99
}

#datos de persona por ejemplo
persona = { #clave - valor
    "1er nombre": "oswaldo",
    "2do nombre": "Lazaro",
}

print(type(producto))
print(type(persona))
#print(dir(producto)) #para ver todos los metodos

print(persona.keys()) #claves
print(persona.items()) #clave-valor

persona.clear()
print(persona) #impirmira el diccionario vacio

#las claves siempre van con dobles comillas
#una lista de diccionarios
productos = [
    {"name": 'libro', "precio":12,},
    {"name": 'otracosa', "precio": 25},
]

print(productos)
