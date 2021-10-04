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