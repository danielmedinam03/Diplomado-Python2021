"""
Solicite un numero de personas 
Llene una lista, cada elemento

Salida: [ nombre 1, nombre 2, nombre 3, nombre n...]
"""
numero=0
numero=int(input("Numero de personas: "))
nombresLista=[]
for i in range (numero):
    name="nombre "+str(i+1)
    nombresLista.append(name)
    print(name)
print(nombresLista)