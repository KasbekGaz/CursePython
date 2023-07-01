x = 40
if x < 30:
    print("x es menor que 30")
else:
    print("x es mayor que 30")

if x == 30 :
    print("El x es igual a 30")
    
# otro ejemplo
color = "verde"
if color  == "rojo":
    print("El color es si es: " + color)
elif color == "verde": #elif comparacion adcional
    print("El color en efecto es: " + color)
else:
    print("el color es otro, en realida es: " + color)

#Otro ejepmlo mas chido

name = "John"
lastname  = "Carter"

if name == "John":
    if lastname == "Carter":
        print("Eres el elegido")
    else:
        print("No eres quien dices que eres")
else: print("nO ERES JOHN")



#Otro ejemplo
#utilizando operadores logicos
x = 12
y = 12
if x > 2 and x <= 10:
    print("x es mayor que 2 y menor o igual que 10")
if x > 2 and x <= 20:
    print("x es mayor que 2 y menor o igual que 20")
if (not(x==y)):
    print("x no es igual a y")
else: print("si es igual")

#aqui agregamos un comentario conchetumare