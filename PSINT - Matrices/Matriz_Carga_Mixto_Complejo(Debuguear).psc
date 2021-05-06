Proceso Matriz_Alumnos_Muestra
	Definir Personajes,Mochila Como Caracter;
	Definir iLong, jLong, iLongMochila, jLongMochila, i, j, im, jm Como Entero;
	Dimension Personajes[999,999];
	Dimension Mochila[2,2];
	iLong<-4;
	iLongMochila<-2;
	jLongMochila<-2;
	i<-0;
	j<-0;
	im<-0;
	jm<-0;
	Escribir "Cantidad de Personajes";
	Leer iLong;
	Para i<-0 Hasta iLong-1 Hacer
		Escribir "Ingresar Personaje ", i+1;
		Escribir "Nombre";
		Leer Personajes[i,0];
		Escribir "Salud";
		Leer Personajes[i,1];
		Escribir "Ataque";
		Leer Personajes[i,2];
		Escribir  "Defensa";
		Leer Personajes[i,3];
		Para im<-0 Hasta iLongMochila-1 Hacer
			Para jm<-0 Hasta jLongMochila-1 Hacer
				Escribir "Ingrese el Item [",im,jm,"] de la mochila;";
				Leer Mochila[im,jm];
			FinPara
		FinPara
	FinPara
	Escribir "----------------------";
	Escribir "----------------------";
	Escribir "----------------------";
	Para i<-0 Hasta iLong-1 Hacer
			Escribir  "Nombre -> ", Personajes[i,0];
			Escribir "Salud -> ", Personajes[i,1];
			Escribir "Ataque -> ", Personajes[i,2];
			Escribir  "Defensa -> ", Personajes[i,3];
			Escribir "----------------------";
			Escribir "Mochila";
			Escribir "----------------------";
			Para im<-0 Hasta iLongMochila-1 Hacer
				Para jm<-0 Hasta jLongMochila-1 Hacer
					Escribir "-----";
					Escribir Mochila[im,jm];
					Escribir "-----";
				FinPara
			FinPara
	FinPara
	Escribir "----------------------";
FinProceso
