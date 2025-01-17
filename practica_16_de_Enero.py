import math


puntoA= []
puntoB= []

valorx1 = int(input("Ingresa el primer punto x1: "))
puntoA.append(valorx1)

valory1 = int(input("Ingresa el Segundo punto y1: "))
puntoA.append(valory1)

valorx2 = int(input("Ingresa el primer punto x2: "))
puntoB.append(valorx2)

valory2 = int(input("Ingresa el Segundo punto y2: "))
puntoB.append(valory2)

p1 = puntoB[0] - puntoA[0]
p2 = puntoB[1] - puntoA[1]

distancia = math.sqrt(p1**2 + p2**2)

print("La distancia es igual a {}".format(distancia))

#Dia 16 archivos
