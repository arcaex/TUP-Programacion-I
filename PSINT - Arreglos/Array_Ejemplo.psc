Algoritmo sin_titulo
	Dimension razas[3]
	Dimension animales[3]
	animales[1] = "Perro"
	animales[2] = "Gato"
	animales[3] = "Paloma"
	Escribir animales[1]
	Escribir animales[2]
	Escribir animales[3]
	Para i<-1 Hasta 3 Hacer
		Escribir "El animal ",i, " es ", animales[i]
	FinPara
	Para i<-1 Hasta 3 Hacer
		Escribir "Ingrese la raza de su preferencia ",1
		Leer razas[i]
	FinPara
	Para i<-1 Hasta 3 Hacer
		Escribir "La Raza ",i," es ",razas[i]
	FinPara
FinAlgoritmo
