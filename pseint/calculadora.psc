Algoritmo Calculadora
	definir num1, num2 Como Real
	Escribir "Calculadora"
	Escribir "Digite el primer numero: "
	Leer num1
	Escribir "Digite el segundo numero: "
	Leer num2
	Escribir "¿Que operacion desea realizar?"
	Escribir "-Si desea realizar una SUMA digite ","1"
	Escribir "-Si desea realizar una RESTA digite ","2"
	Escribir "-Si desea realizar una DIVISION digite ","3"
	Escribir "-Si desea realizar una MULTIPLICACION digite ","4"
	Leer op
	Si op == 1 Entonces
		resultado=num1+num2
		Escribir "Resultado: ", resultado
	FinSi
	Si op == 2 Entonces
		resultado=num1-num2
		Escribir "Resultado: ", resultado
	FinSi
	Si op == 3 Entonces
		si num2 == 0 Entonces
			Escribir "ERROR!! Division en cero"
		SiNo
			resultado=num1/num2
			Escribir "Resultado: ", resultado
		FinSi
		
	FinSi
	Si op == 4 Entonces
		resultado=num1*num2
		Escribir "Resultado: ", resultado
	FinSi
	
FinAlgoritmo
