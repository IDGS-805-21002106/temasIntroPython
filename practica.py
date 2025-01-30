import os
from io import open

class Cine:
    def __init__(self):
        self.boletos = 0
        self.boletos_posibles = 0
        self.precio_por_boleto = 12 
        self.total = 0
        self.personas = 0
        self.compras = []  
        self.total_sesion = 0 
        self.nombre = "" 

    def compra(self, boletos, descuento):
        total_compra = boletos * self.precio_por_boleto
        total_compra -= total_compra * descuento
        op2 = int(input("¿Desea realizar la compra con tarjeta CINECO? \n1- SI \n2- NO: "))
        if op2 == 1:
            total_compra -= total_compra * 0.10
        
        print(f"\nGRACIAS POR SU COMPRA, {self.nombre}")
        print(f"Su total es de: ${total_compra:.2f} y su cantidad de boletos es de: {boletos}")
        
        self.compras.append(f"Nombre: {self.nombre}\nBoletos: {boletos}\nTotal: ${total_compra:.2f}\n--------------\n")
        self.total_sesion += total_compra

    def descuent(self, boletos):
        if boletos > 5:
            return 0.15
        elif 3 <= boletos <= 5:
            return 0.10
        else:
            return 0

    def guardar_ticket(self):
        with open('fichero.txt', 'w') as fichero:
            for compra in self.compras:
                fichero.write(compra)

    def imprimir_ticket(self):
        with open('fichero.txt', 'r') as fichero:
            contenido = fichero.read()
            print("\nCOMPRAS REALIZADAS:")
            print(contenido)

    def inicio(self):
        print("\nBIENVENIDO A CINEPOLIS")
        continuar = True
        while continuar:
            self.nombre = input("Por favor, introduzca su nombre: ")
            self.personas = int(input("\nCuantas personas van a comprar boletos? "))
            self.boletos_posibles = self.personas * 7
            
            while True:
                boletos = int(input("Cuántos boletos desea comprar? "))
                
                if boletos > self.boletos_posibles:
                    print("No puedes comprar más de 7 boletos por persona.")
                    print("Seleccione una opción:")
                    print("1. Cambiar el número de personas.")
                    print("2. Cambiar cantidad de boletos.")
                    opcion = int(input("Opción: "))
                    
                    if opcion == 1:
                        self.personas = int(input("¿Cuántas personas van a comprar boletos? "))
                        self.boletos_posibles = self.personas * 7
                        if boletos > self.boletos_posibles:
                            print(f"El número de boletos que desea comprar ({boletos}) excede el número máximo permitido de boletos ({self.boletos_posibles}).")
                            continue
                        break
                    elif opcion == 2:
                        continue
                else:
                    break

            descuento = self.descuent(boletos)
            self.compra(boletos, descuento)

            opcion = int(input("\nDesea realizar otra compra? \n1- SI \n2- NO: "))
            if opcion == 1:
                os.system('cls')
            else:
                continuar = False
                print("\nGracias por su compra")
        
        self.guardar_ticket()
        self.imprimir_ticket()
        print(f"\nTotal de compras: ${self.total_sesion:.2f}")

def main():
    cine = Cine()
    cine.inicio()

if __name__ == "__main__":
    main()
