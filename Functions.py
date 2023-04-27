def mifuncion():
	print('Hola mirame soy una funcion xd')
# La llamamos asi:
mifuncion()

##### Ejemplo 2
def mifuncion(name = "Persona desconocida"):
	print('Hola, mirame soy una funcion xd, como estas ' + name +'?')
# La llamamos asi:
mifuncion('Oswaldo') #aqui pasamos el parametro de name o sea el nombre
# podemos reutilizar el codgo de funcion
mifuncion('Carlos')
# si no le pasamos nada?
#nos dara error si no definimos un valor por defecto asi que mejor definimos un valor cuando no se agrega nada
#name = 'Persona'
#y cuando la llamemos a llamar sin nada daria ese dato
mifuncion()
#### unsa sumatoria para retornar un valor
def sumar(numero1, numero2):
	return numero1 + numero2
print(sumar(12,12)) #la salida seria 24
print(sumar(90,10)) #podemos mandar otro dato. salida 100
# aqui hay otro que la neta si que hacia
add = lambda n1 ,n2 : n1 +n2 
print(add(12,34))




