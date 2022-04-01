Proceso Matriz_Ejercicio_Ajedrez
	Definir Tablero Como Caracter;
	Definir iLong, jLong, i, j, iLongJugada Como Entero;
	Dimension Tablero[999,999];
	iLong<-8;
	jLong<-8;
	iLongJugada<-3;
	Para i=1 Hasta iLong Hacer
		Para j=1 Hasta jLong Hacer
			Tablero[i,j] = "-";
		FinPara
	FinPara
	Tablero[7,7]="[r,B]";
	Tablero[7,6]="[R,B]";
	Tablero[6,3]="[r,N]";
	Tablero[2,5]="[R,N]";
	f = 2;
	c = 5;
	Para i<-1 Hasta iLongJugada Hacer
		Tablero[f,c]=" ";
		f = f+1;
		c = c-1; 
		Tablero[f,c]="[R,N]";
		Escribir "Reina en Posicion -> [",f,",",c,"]";
	FinPara
	Para i=1 Hasta iLong Hacer
		Para j=1 Hasta jLong Hacer
			Escribir "[",i,",",j,"] -> ",Tablero[i,j],Sin Saltar;
		FinPara
		Escribir " ";
	FinPara
FinProceso