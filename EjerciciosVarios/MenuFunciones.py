i = 0
uLiquido = 0
volumenFinal=0
indice=0
def operacion(numero1, numero2, opcion):
    
    if opcion == 1:
        resultado = numero1+numero2
        print("resultado: ", resultado)
    elif opcion == 2:
        resultado = numero1-numero2
        print("resultado: ", resultado)
    elif opcion == 3:
        if numero2 == 0:
            print("No se puede dividir en 0")
        else:
            resultado = numero1/numero2
            print("resultado: ", resultado)
    elif opcion == 4:
        resultado = numero1*numero2
        print("resultado: ", resultado)

def unidadDeMedidaVolumen(uLiquido,volumenFinal,opc):
    volumenFinal=0
    x=0
    opc=int(opc)
    uLiquido=int(uLiquido)
    if opc == 1:

        while x<1:
            opcUnidadVolumen = int(input("""
                                    1. Si desea convertir de Litros a Galones
                                    2. Si desea convertir de Litros a Pintas
                                    Opcion: """))
            if opcUnidadVolumen >=1 and  opcUnidadVolumen <=2:
                

                if opcUnidadVolumen==1:
                    volumenFinal = uLiquido*2.6417
                    print(uLiquido, " litros equivalen a ", volumenFinal, " galones")
                elif opcUnidadVolumen==2:
                    volumenFinal = uLiquido*2.11338
                    print(uLiquido, " litros equivalen a ", volumenFinal, " pintas")
                else: 
                    print()
                x+=1
            else:
                print("ERROR!! Estas digitando una letra o un numero no correspondiente")
    elif opc == 2:
        while x<1:
            opcUnidadVolumen = int(input("""
                                    1. Si desea convertir de Galones a Litros
                                    2. Si desea convertir de Galones a Pintas
                                    Opcion: """))
            if opcUnidadVolumen >=1 and  opcUnidadVolumen <=2:
                opcUnidadVolumen=int(opcUnidadVolumen)

                if opcUnidadVolumen==1:
                    volumenFinal = 3.7854118*uLiquido
                    print(uLiquido, " galones equivalen a ", volumenFinal, " litros")
                elif opcUnidadVolumen==2:
                    volumenFinal = uLiquido*8
                    print(uLiquido, " galones equivalen a ", volumenFinal, " pintas")
                else:
                    print()
                x+=1
            else:
                print("ERROR!! Digite un numero")
        
    elif opc == 3:
        while x<1:
            
            opcUnidadVolumen = int(input("""
                                    1. Si desea convertir de Pintas a Litros
                                    2. Si desea convertir de Pintas a Galones
                                    Opcion: """))
            if opcUnidadVolumen >=1 and  opcUnidadVolumen <=2:
                
                if opcUnidadVolumen==1:
                    volumenFinal = 0.57*uLiquido
                    print(uLiquido, " pintas equivalen a ", volumenFinal, "  litros")
                elif opcUnidadVolumen==2:
                    volumenFinal = uLiquido*0.125
                    print(uLiquido, " pintas equivalen a ", volumenFinal, " galones")
                else:
                    print()
                x+=1
            else:
                print("ERROR!! Digite un numero")

        
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

def unidadesDistancia(opcUnidadLongitud, longitud):
    opcUnidadLongitud=int(opcUnidadLongitud)
    longitud=int(longitud)
    if opcUnidadLongitud ==1:
        unidadFinal=longitud/100
        print("Resultado: ",unidadFinal," metros")
    elif opcUnidadLongitud==2:
        unidadFinal=longitud/612371
        print("Resultado: ",unidadFinal," Millas")
    elif opcUnidadLongitud==3:
        unidadFinal=longitud/100000
        print("Resultado: ",unidadFinal," Kilometros")
    elif opcUnidadLongitud==4:
        unidadFinal=longitud*100
        print("Resultado: ",unidadFinal," Centimetros")
    elif opcUnidadLongitud==5:
        unidadFinal=longitud/6213.71
        print("Resultado: ",unidadFinal," Millas")        
    elif opcUnidadLongitud==6:
        unidadFinal=longitud/1000
        print("Resultado: ",unidadFinal," Kilometros")
    elif opcUnidadLongitud==7:
        unidadFinal=longitud*160934
        print("Resultado: ",unidadFinal," centimetros")
    elif opcUnidadLongitud==8:
        unidadFinal=longitud*1609.34
        print("Resultado: ",unidadFinal," metros")
    elif opcUnidadLongitud==9:
        unidadFinal=longitud*1.609
        print("Resultado: ",unidadFinal," Kilometros")
    elif opcUnidadLongitud==10:
        unidadFinal=longitud*100000
        print("Resultado: ",unidadFinal," Centimetros")
    elif opcUnidadLongitud==11:
        unidadFinal=longitud*1000
        print("Resultado: ",unidadFinal," Metros")
    elif opcUnidadLongitud==12:
        unidadFinal=longitud/1.609
        print("Resultado: ",unidadFinal," Millas")
    """
    1cm = 0.01m
    1cm = 0.00001km
    1cm = 0.00000621371

    1m = 100cm
    1m = 0.001km
    1m = 0.000621371 millas

    1milla = 1.60934km
    1milla = 1609.34m
    1milla = 160934cm

    1km = 0.621371 millas
    1km = 1000m
    1km = 100000cm
    """
#Menu de opciones
#While, para que se quede en el bucle hasta que el usuario digite una opción correcta
while i <=1:
    opcMenu = (input("""Menú:
              1. Calculadora
              2. Unidad de medida Liquidos
              3. Promedio Sueldos
              4. Unidades de distancia
              SI DESEAS SALIR DIGITA UN '*'
              Opcion: """))
    
    #Validacion que sea un numero 
    
    if opcMenu.isnumeric()==True:
        #Convierte el numeor en un entero
        opcMenu = int(opcMenu)
        if opcMenu>=1 and opcMenu<=4 :
            x=0
            #Condicionales para realizar las diferentes opciones del menú
            if opcMenu == 1:
                
                while x <1:
                    numero1 = (input("Digite numero 1: "))
                    numero2 = (input("Digite numero 2: "))

                    opcion = (input("Si desea realizar una suma digite 1: \n" +
                        "Si desea realizar una resta digite 2: \n" +
                        "Si desea realizar una division digite 3: \n" +
                        "Si desea realizar una multiplicacion digite 4: \n" +
                        "Opcion: "))
                    
                    #Validacion que sea un numero 

                    if numero1.isnumeric() == True and numero2.isnumeric() == True and opcion.isnumeric() == True:
                        """
                        numero1:int=numero1
                        numero2:int=numero2
                        opcion:int=opcion
                        """
                        numero1=int(numero1)
                        numero2=int(numero2)
                        opcion=int(opcion)
                        if opcion>=1 and opcion<=4:
                            x+=1
                            operacion(numero1, numero2, opcion)
                        
                    else:
                        print("ERROR !!! Estas digitando letras o un numero no correspondiente ")
            #Condicion para realizar la unidad de Volumen
            elif opcMenu == 2:
                opc = (input("""Digite el numero segun corresponda:
                            Que unidad de medida desea convertir ?
                            
                            1. Si desea convertir Litros
                            2. Si desea convertir Galones
                            3. Si desea convertir Pintas
                            Opción: """))
            
                uLiquido = (
                    input("Volumen de liquido que desea convertir: "))
                
                #Validacion que sea un numero
                if opc.isnumeric()==True and uLiquido.isnumeric()==True:
                          
                    unidadDeMedidaVolumen(uLiquido,volumenFinal,opc)
            #Condicion para realizar el promedio de sueldos
            elif opcMenu==3:
                
                numPersonas=input("Ingrese el numero de personas: ")
                if numPersonas.isnumeric()==True:
                    
                    promedioSueldos(numPersonas)
            #Condicion para realizar la conversion de medida del unidad de Longitud
            elif opcMenu==4:
                
                longitud=input("Longitud que desea convertir: ")
                opcUnidadLongitud=(input("""
                                  Digite el numero segun corresponda.
                                1. Si desea convertir de Centimetros a Metros
                                2. Si desea convertir de Centimetros a Millas
                                3. Si desea convertir de Centimetros a Kilometros
                                4. Si desea convertir de Metros a Centimetros
                                5. Si desea convertir de Metros a Millas
                                6. Si desea convertir de Metros a Kilometros
                                7. Si desea convertir de Millas a Centimetros
                                8. Si desea convertir de Millas a Metros
                                9. Si desea convertir de Millas a Kilometros
                                10. Si desea convertir de Kilometros a Centimetros
                                11. Si desea convertir de Kilometros a Metros
                                12. Si desea convertir de Kilometros a Millas
                                """))
                if longitud.isnumeric()==True and opcUnidadLongitud.isnumeric()==True:
                    
                    unidadesDistancia(opcUnidadLongitud, longitud)
            
            # Contador para salir del menú
            i += 1
    
    #Dar mensaje cuadno la opción no es correcta
    else:
        print("")
    
    if opcMenu=="*":
        break




