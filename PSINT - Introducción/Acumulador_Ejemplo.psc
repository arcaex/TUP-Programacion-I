Algoritmo sin_titulo
	acumulador = 0
	nota = 0
	Para i<-1 Hasta 3 Hacer
		Mientras nota=0 Hacer
			Escribir "Ingrese la nota ",i
			Leer nota
		FinMientras
		acumulador = acumulador + nota
		Escribir acumulador
	FinPara
	promedio = acumulador/3
	Escribir "El promedio es ", promedio
FinAlgoritmo
