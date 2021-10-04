import os

#Ruta del directorio
ruta = os.getcwd()
print("-----",ruta,"-----")
#Pregunta si es un archivo
print(os.path.isfile("ManejoArchivos.py"))
#Pregunta si es un directorio
print(os.path.isdir("ManejoArchivos.py"))

