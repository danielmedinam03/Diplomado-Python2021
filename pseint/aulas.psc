Algoritmo aulas
	definir val como Entero
	
	Escribir "Valoracion: "
	Leer val
	Si val>=0 y val<=75 Entonces
		Escribir "Valoraci�n del aula POR MEJORAR"
		Escribir "Deben enviar un correo electronico al docente indicanto el proceso de mejora"
	FinSi
	Si val>75 y val<=84 Entonces
		Escribir "Valoraci�n del aula ACEPTABLE"
	FinSi
	Si val>84 y val<=94 Entonces
		Escribir "Valoraci�n del aula BUENO"
	FinSi
	Si val>94 Entonces
		Escribir "Valoraci�n del aula EXCELENTE"
	FinSi
	
FinAlgoritmo
