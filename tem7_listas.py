#Listas

lista1 = [10, 5, 3]
lista2 = [1.5, 2.66, 1.70, 89.2]
lista3 = ["lunes", "martes", "miercoles"]
lista4 = ["juan", 45.1, 1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0])

suma=0
x=0
while x < len(lista1):
    suma = suma + lista1[x]
    x=x+1

print("La suma es {}".format(suma))

print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

lista5= []

for x in range(5):
    valor = int(input("Ingresa un valor: "))
    lista5.append(valor)

print(lista5)

#Eliminar elementos de una lista
print(lista1)
lista1.pop()
print(lista1)

#Ejercicio / que imprima la lista con n nuemros, que imprama numeros impares y impares
listaEjer= []
numeros = int(input("Ingrese la cantidad de numeros a ingresar: "))
i=0
pares=0
impares=0
for i in range(numeros):
    
    num = int(input("Ingresa un valor: "))
    listaEjer.append(num)
    if num%2 == 0:
        pares= pares+1
    else:
        impares = impares+1

print(listaEjer)
print("El numero de numeros pares es {} y el numero de numeros impares es: {}".format(pares, impares))


#funciones de lista

lista1.sort() #Ordenar la lista
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove
print(lista1) #?

lista1.clear()
print(lista1)#?


