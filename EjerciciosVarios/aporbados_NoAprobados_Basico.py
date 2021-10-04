
n = int(0)
aprobados = int(0)
nAprob = int(0)
reprobados = int(0)
nReprob = int(0)
cont = int(0)
nota:float=0
porcA:float = 0
porcR:float=0
n = int(input("Numero de Estudiantes: "))

if  n <= 0 :
    print("ERROR !!")
else: 
    while (cont<n):
        nota=float(input("Nota: "))
        cont+=1
        if (nota>5 or nota <0):
            print("ERROR!! La nota debe ser mayor a 0 y menor que 5")
        else:
            if ((nota>=3 and nota<=5)):
                    nAprob +=1
                    if (nota>5 or nota <0):
                        nAprob-=1         
                    aprobados+=nota
                    porcA=(100*nAprob)/n
            elif ((nota>=0 and nota<3)):
                    nReprob+=1
                    if (nota>5 or nota <0):
                        nReprob-=1    
                    reprobados+=nota
                    porcR=(100*nReprob)/n
        
print("Aprobados: ",nAprob,"Porcentaje: ",porcA,"%")
print("Reprobados: ",nReprob,"Porcentaje: ",porcR,"%")
x=nAprob+nReprob
if n != x:
    estu = n-x
    if estu==1:
        print("HAY ERROR EN: ",estu,"Estudiante")
    else:    
        print("HAY ERROR EN: ",estu,"Estudiantes")