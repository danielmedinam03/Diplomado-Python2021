def ingresoDatos():
    global numero1,numero2, opcion
    numero1 = 0  # primer numero digitado por usuario
    numero2 = 0  # segundo numero digitado por usuario
    # ingreso de numeros    
    numero1 = int(input("Digite numero 1: "))
    numero2 = int(input("Digite numero 2: "))
    # Meno de opciones
    opcion = int(input("Si desea realizar una suma digite 1: \n" +
                    "Si desea realizar una resta digite 2: \n" +
                    "Si desea realizar una division digite 3: \n" +
                    "Si desea realizar una multiplicacion digite 4: \n" +
                    "Opcion: "))
ingresoDatos()
    
def operacionesMenu(opcion,numero1,numero2):
    if (opcion) == 1:
        suma = (numero1)+(numero2)
        print("Resultado: ", suma)
    elif (opcion)==2:
        resta=(numero1)-(numero2)            
        print("Resultado: ",resta)
    elif (opcion)==3:
        if (numero2)==0:
            print("No se puede dividir en 0")
        else:
            division= (numero1)/(numero2)
            print("Resultado: ",division)
    elif (opcion)==4:
        multiplicacion=(numero1)*(numero2)
        print("Resultado: ",multiplicacion)
operacionesMenu(opcion,numero1,numero2)

