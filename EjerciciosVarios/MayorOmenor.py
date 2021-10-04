numero1=float(input("Numero 1: "))
numero2=float(input("Numero 2: "))

def PositivoNegativo(numero1,numero2):
    if numero1<0 :
        print("El numero ",numero1, "es negativo")
    else:
        print("El numero ",numero1, "es positivo")
    
    if numero2<0:
        print("El numero ",numero2, "es negativo")
    else:
        print("El numero ",numero2, "es positivo")

if numero1>numero2:
    print("EL numero 1: ",numero1, " es mayor que el numero 2")
    PositivoNegativo(numero1, numero2)
elif numero1<numero2:
    print("EL numero 2: ", numero2 ," es mayor que el numero 1")
    PositivoNegativo(numero1, numero2)

