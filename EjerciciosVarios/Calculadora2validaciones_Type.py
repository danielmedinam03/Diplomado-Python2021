"""
numero1 = 0  # primer numero digitado por usuario
numero2 = 0  # segundo numero digitado por usuario
# ingreso de numeros
numero1 = (input("Digite numero 1: "))
numero2 = (input("Digite numero 2: "))

# Meno de opciones
opcion = int(input("Si desea realizar una suma digite 1: \n" +
                   "Si desea realizar una resta digite 2: \n" +
                   "Si desea realizar una division digite 3: \n" +
                   "Si desea realizar una multiplicacion digite 4: \n" +
                   "Opcion: "))

if numero1.isnumeric() == True and numero2.isnumeric()==True:
    numero1=float(numero1)
    numero2=float(numero2)
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
else:
    print("Digite solamente numeros.")
"""
numero1 = 0  # primer numero digitado por usuario
numero2 = 0  # segundo numero digitado por usuario
# ingreso de numeros
def ingresoDatos():
    global numero1,numero2,opcion
    numero1 = (input("Digite numero 1: "))
    numero2 = (input("Digite numero 2: "))

    # Meno de opciones
    opcion =(input("Si desea realizar una suma digite 1: \n" +
                   "Si desea realizar una resta digite 2: \n" +
                   "Si desea realizar una division digite 3: \n" +
                   "Si desea realizar una multiplicacion digite 4: \n" +
                   "Opcion: "))
def operacionesMenu():
    
    if numero1.isnumeric() == False or numero2.isnumeric()== False or opcion.isnumeric()==False:
        while 
            ingresoDatos()