#Inicialización de variables
numero1=0
numero2=0
numero3=0
#Variables de entrada
numero1=float(input("Numero 1: "))
numero2=float(input("Numero 2: "))
numero3=float(input("Numero 3: "))
#Validaciones
if numero1==numero2 and numero2==numero3 and numero1==numero3:   
    print("Todos los numeros son igules.")
elif numero1!=numero2 and numero1!=numero3 and numero2!=numero3:
    print("Todos los numeros son diferentes.")
else:
    print("Hay dos numeros iguales")
