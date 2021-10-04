"""
Realice el codigo para calcular el promedio de las calificaciones de un grupo N
de estudiantes del curso de progrmación 
"""

n: int = 0
i: int = 0
acum: float = 0
final_nota: float = 0
n=int(input("Numero de estudiantes: "))
if n <= 0:
    print("ERROR!!!  Almenos debe haber un estudiante")
else:
    while i <n:
        i+=1 
        nota=float(input("Nota: "  ))
        acum= nota + acum
        final_nota=acum/n
    print("Acumulado de notas: ",acum)
    print("promedio: ",final_nota)

