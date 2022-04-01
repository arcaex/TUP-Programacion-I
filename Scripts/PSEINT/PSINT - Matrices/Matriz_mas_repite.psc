Proceso Matriz_mas_repite
	Definir Animales,MasRepetido Como Caracter;
	Definir iLong,jLong, Aux, i, j, im, jm, Acumulador Como Entero;
	Dimension Animales[9999,9999];
	Animales[0,0]<-"Perro";
	Animales[0,1]<-"Gato";
	Animales[1,0]<-"Conejo";
	Animales[1,1]<-"Conejo";
	Animales[2,0]<-"Gato";
	Animales[2,1]<-"Conejo";
	Animales[3,0]<-"Gato";
	Animales[3,1]<-"Gato";
	Aux<-0;
	MasRepetido<-"";
	Acumulador<-0;
	iLong<-4;
	jLong<-2;
	Para i<-0 Hasta iLong-1 Hacer
		Para j<-0 Hasta jLong-1 Hacer
			Para im<-0 Hasta iLong-1 Hacer
				Para jm<-0 Hasta jLong-1 Hacer
					Si Animales[i,j]=Animales[im,jm] Entonces
						Acumulador<-Acumulador+1;
					FinSi
				FinPara
				Si Acumulador>Aux Entonces
					MasRepetido<-Animales[i,j];
					Aux<-Acumulador;
				FinSi
				Acumulador<-0;
			FinPara
		FinPara
	FinPara
	Escribir "El animal que más se repite es: ", MasRepetido;
FinProceso
