
with open("SegundoArchivo.txt", "r+",encoding="utf-8") as archivo:
    #archivo.write(" Hola Como estan ? ")
    
    #archivo.write("Mi nombre es daniel")
    escribir = input("Digite que desea escribir: ")
    archivo.write(escribir + "\n")
    
    
    leer=archivo.readlines()
    print(leer)
archivo.close()