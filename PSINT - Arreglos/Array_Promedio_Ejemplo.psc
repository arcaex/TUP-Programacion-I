Algoritmo sin_titulo
	acumulador <- 0
	Escribir 'Ingrese cantidad de notas'
	Leer n
	Dimension notas[n]
	Para i<-1 Hasta n Hacer
		Escribir 'Ingrese la nota numero ',i
		Leer notas[i]
		acumulador <- acumulador+notas[i]
	FinPara
	promedio <- acumulador/n
	Escribir 'El promedio es igual a ',promedio
FinAlgoritmo
