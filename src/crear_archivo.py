# Escritura y creacion del archivo.
archivo = open("archivo.txt", "w")
archivo.write(f"Hola mundo!\n")
archivo.close()

# Modificacion del archivo, agregando una linea al final.
archivo = open("archivo.txt", "a")
archivo.write(f"Este mensaje esta abajo de la linea anterior.\n")
archivo.close()

# Lectura del archivo e impresion de las líneas.
with open("archivo.txt", "r") as archivo:
    while linea := archivo.readline().rstrip():
        print(linea)
