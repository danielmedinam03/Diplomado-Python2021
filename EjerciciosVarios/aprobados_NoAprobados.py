n = int(0)
aprobados = int(0)
nAprob = int(0)
reprobados = int(0)
nReprob = int(0)
cont = int(0)
newCount = int(0)
nota:float=0
porcA:float = 0
porcR:float=0
newNota:float=0
newAprobados:float=0
newReprobados:float=0
promAprob:float=0
promReprob:float=0
n = int(input("Numero de Estudiantes: "))

if  n <= 0 :
    print("ERROR !!")
else: 
    while (cont<n):
        nota=float(input("Nota: "))
        cont+=1
        if (nota>5 or nota <0):
            print("ERROR!! La nota debe ser mayor a 0 y menor que 5")
            newNota=float(input("Ingrese de nuevo la nota: "))
            newCount+=1
        
        else:
            
            if (newCount>0):            
                if ((nota>=3 or nota<=5)or(newNota>=3 or newNota<=5)):
                    nAprob +=1
                    aprobados+=nota
                    newAprobados+=newNota
                    promAprob = (aprobados + newAprobados) / nAprob
                    porcA=(100*nAprob)/n
                elif ((nota>=0 or nota<3)or(newNota>=0 or newNota<3)):
                    nReprob+=1
                    reprobados+=nota
                    newReprobados+=newNota
                    promReprob = (reprobados + newReprobados) / nReprob
                    porcR=(100*nReprob)/n
        
print("Aprobados: ",nAprob,"Porcentaje: ",porcA,"%","Promedio Aprobados: ",promAprob)
print("Reprobados: ",nReprob,"Porcentaje: ",porcR,"%","Promedio Reprobados: ",promReprob)
