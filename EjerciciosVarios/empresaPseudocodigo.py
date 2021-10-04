""""El gerente de una empresa desea un pseudocodigo que calcule el aumento de sueldo
para un grupo de n empleados teniendo en cuenta los siguiendtes criterios, si el sueldo
es inferior a 5000 pesos el aumento sera del 10%, si el sueldo es superior a 5000 pesos
el aumneto sera de 8%. imprima el nuevo sueldo del trabajador y el total de la nomina de
la empresa."""


cont: int = 0
nomina: float = 0
n = 0
while n <= 0:
    n = int(input("Numero de empleados: "))
    if n<=0:
        print("Digite un valor mayor a 0")
        
    else:
        while cont < n:
            cont += 1
            sueldo = float(input("Sueldo : "))
            if sueldo < 5000:
                aumento: float = sueldo*0.1
                newSueldo: float = sueldo + aumento
                nomina += newSueldo
                print("Nuevo sueldo: ", newSueldo)
            elif sueldo > 5000:
                aumento: float = sueldo*0.08
                newSueldo: float = sueldo + aumento
                nomina += newSueldo
                print("Nuevo sueldo: ", newSueldo)
            elif sueldo==5000:
                cont=cont-1
                print("Nadie en esta empresa gana $5000",cont)
            else:
                print("ERROR!!")
        print("Nomina de la empresa: ", nomina)
    