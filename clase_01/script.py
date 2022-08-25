'''respuesta = 0
#falta verificar

comentario
en varias
lineas (son comillas simples)


while (True):
    respuesta = input("Numero? ")
    respuesta = int(respuesta)
   # if (respuesta == 1): break #se comporta como un while porque antes de solicitar algo, pregunta

    if (respuesta == 10):
        print("Es 10")
    elif (respuesta == 11):
        print("Es 11")
    else:
        print("No es 10")
        
    if (respuesta == 1):  #se comporta como do whhile
        break              #pregunta que define si se rompe o no la iteracion
    
'''
#iterable funcion con grado de memoria 
#los for de python saben recorrer nombres, en casa iteración agarre uno (permite ir recorriendo listas de cosas)
#for recorre elementos iterables
'''
lista_numeros = [33.3, "HOLA", 1, 2, 3, 4, 5, 6]
for numero in lista_numeros:
    print(numero)
#recorre listas sin importar tipo de dato

lista_numeros = list (range(100))
for numero in lista_numeros:
    print(numero)

for numero in range(20):
    print(numero)
    #print(id(numero)) identificar de lugares en memoria
    
numero = 0
while numero < 20:
    print(numero)
    numero +=1

#lista, agregar a listas
lista_nombres = []
while True:
    nombre = input("Nombre?")
    lista_nombres.append(nombre)
    
    respuesta = input("para salir presione (s)")
    if (respuesta == 's'):
        break
   
for nombre in lista_nombres:
    print(nombre) 
'''
lista_nombres = []
for i in range(5):
    nombre = input("Nombre? : ")
    lista_nombres.append(nombre)


for nombre in lista_nombres:
    print(nombre)    