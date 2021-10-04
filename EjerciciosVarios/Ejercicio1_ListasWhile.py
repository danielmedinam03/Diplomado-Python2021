numero=0
numero=int(input("Numero de personas: "))
nombresLista=[]
i=0
while i < numero:
    name="nombre "+str(i+1)
    nombresLista.append(name)
    print(name)
    i+=1
print(nombresLista)
print(len(nombresLista))
