def promedioSueldos(numPersonas,indice=0,acumuladorSueldo=0):

    if numPersonas.isnumeric()==True:
        numPersonas=int(numPersonas)
        while indice<numPersonas:
            sueldo=float(input("Ingrese sueldo: $"))
            acumuladorSueldo+=sueldo
            finalPromedio=acumuladorSueldo/numPersonas
            indice+=1
        print("Promedio de sueldos: $",finalPromedio)
    else:
        print("ERROR !!! Digite por favor un nuemero")
