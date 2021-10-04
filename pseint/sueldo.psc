Algoritmo Sueldo
	Definir vHora, sldo, seg_social, total,totalF, boni Como Real
	Definir hTrj Como Entero
	Definir nom Como Caracter
	vHora=0
	sldo=0
	seg_social=0
	total=0
	totalF=0
	boni=0
	
	Escribir "Nombre del Empleado: "
	Leer nom
	Escribir "Horas Trabajadas: "
	Leer hTrj
	Escribir "Valor por hora: "
	Leer vHora
	
	//Calculos
	sldo = hTrj * vHora
	seg_social = sldo*0.33
	total = sldo - seg_social
	Si hTrj > 0 Entonces
		Si vHora > 0 Entonces
			
			Si sldo < 300000 Entonces
				boni= total * 0.02
				totalF = total + boni
			SiNo
				totalF = total
			FinSi
			Escribir "El sueldo del empleado ", nom
			Escribir "es de: $", totalF
		SiNo
			Escribir "No es posible realizar el calculo Digite el valor de la hora en numero positivo"
		FinSi
	SiNo
		Escribir "No es posible realizar el calculo Digite el numero de horas trabajadas en positivo"
	FinSi
FinAlgoritmo
