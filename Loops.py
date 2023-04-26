#Si por ejeplo queremos mandar imprimir estos datos podraimos hacerlo mandadndo a llamar por sus indice
#Pero cuando quisieramos agregar un dato mas tendriamos que escribir otro print y el indice correspodiente a el item.

comidas = [ 'manzanas', 'pan', 'queso', 'leche', 'platanos', 'añadiendonuevoitem']
# print(comidas[0])
# print(comidas[1])
# print(comidas[2])
# print(comidas[3])
# print(comidas[4])
# print(comidas[5]) #el nuevo item

#Como imprimirria datos de 1000000000 de items
#pues con lo siguiente:
# se usa un for apra recorrer el dato
for comida in comidas:
    if comida == "queso":
        print("compra esto pq ya no hay")
        #break #romper el recorrido del for
        continue #ignora la condicion anterior pero continua con el recorrido
    print(comida)


## Podemos ahcer tambien lo siguiente:
# imprimir un rango
for numeros in range(1,8):
    print(numeros) #imprime nuemros en el rango indicado este caso del 1 al 7
    #nota: que el segundo numero no lo cuenta para impirmir debido a que cuenta en indice
    #desde 0 en adelante 0 = 1 1=2 y asi por eso la salida es unicamente hasta 7

# tambien puedes hacer esto
for letra in "Hola hijo de la chingada" :
    print(letra)


#tambien podemos usar este llamado WHILE
#Hacer contar hasta llegar un determinado valor
#le decimos cuenta desde 4
contar = 4

while contar <= 10 :
    print(contar) #va imprimir el valor
    contar = contar + 1 #va sumar el dato 1 para llegar a 10
#cuando llegue a 10 dejara de hacerlo? En efecto
