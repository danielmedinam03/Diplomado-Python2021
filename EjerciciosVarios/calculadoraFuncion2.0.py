numero1=float(input("Digite numero 1: "))
numero2=float(input("Digite numero 2: "))
opcion=int(input("Si desea realizar una suma digite 1: \n"+
                 "Si desea realizar una resta digite 2: \n"+
                 "Si desea realizar una division digite 3: \n"+ 
                 "Si desea realizar una multiplicacion digite 4: \n"+
                 "Opcion: "))

def operacion(numero1, numero2, opcion):
    if opcion==1:
        resultado=numero1+numero2
        print("resultado: ", resultado) 
    elif opcion==2:
        resultado=numero1-numero2
        print("resultado: ", resultado) 
    elif opcion==3:
        if numero2==0:            
            print("No se puede dividir en 0")
        else:
            resultado=numero1/numero2
            print("resultado: ", resultado) 
    elif opcion==4:
        resultado=numero1*numero2
        print("resultado: ", resultado) 
operacion(numero1,numero2, opcion)

print(type(numero1))
