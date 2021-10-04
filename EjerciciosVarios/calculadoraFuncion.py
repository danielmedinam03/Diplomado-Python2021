
numero1=0 #primer numero digitado por usuario
numero2=0 #segundo numero digitado por usuario
#ingreso de numeros
numero1=float(input("Digite numero 1: "))
numero2=float(input("Digite numero 2: "))
#Meno de opciones 
opcion=int(input("Si desea realizar una suma digite 1: \n"+
                 "Si desea realizar una resta digite 2: \n"+
                 "Si desea realizar una division digite 3: \n"+ 
                 "Si desea realizar una multiplicacion digite 4: \n"+
                 "Opcion: "))
def suma(numero1,numero2):
    return numero1+numero2
def resta(numero1,numero2):
    return numero1-numero2
def division(numero1,numero2):
    if numero2==0:
        print("No se puede dividir en 0")
    else:
        return numero1/numero2
def multiplicacion(numero1,numero2):
    return numero1*numero2
#Resultados
if opcion==1:
    print("Resultado: ",suma(numero1,numero2))
elif opcion==2:
    print("Resultado: ",resta(numero1,numero2))
elif opcion==3:
    print("Resultado: ",division(numero1,numero2))
elif opcion==4:
    print("Resultado: ",multiplicacion(numero1,numero2))