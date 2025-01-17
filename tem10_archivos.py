#ARCHIVOS

from io import open

texto = "Una linea con texto\n otra linea de texto"
fichero = open('fichero.txt', 'w')
fichero.write(texto)

cadena2 = "\nEsto es otra Cadena"
fichero.write(cadena2)
fichero.close()

cadena3 = "\nEsto es otra Cadena"
fichero.write(cadena3)
