Proceso Matriz_Ejercicio_Ajedrez
	Definir Tablero Como Caracter;
	Definir iLong, jLong, i, j, iLongJugada Como Entero;
	Dimension Tablero[999,999];
	iLong<-8;
	jLong<-8;
	iLongJugada<-3;
	
	/// Cargo todo el tablero en Blanco
	Para i<-1 Hasta iLong Hacer
		Para j<-1 Hasta jLong Hacer
			Tablero[i,j]<-" ";
		FinPara
	FinPara
	
	/// Inicializo las piezas en el Tablero
	Tablero[7,7]<-"Rey Blanco";
	Tablero[7,6]<-"Reina Blanca";
	Tablero[6,3]<-"Rey Negro";
	Tablero[2,5]<-"Reina Negra";
	
	/// Realizo el movimiento de la Reina
	Para i<-1 Hasta iLongJugada Hacer
		/// Movimiento Diagonal
		Tablero[2+i,5-i]<-"Reina Negra";
		/// Borro el movimiento anterior
		Tablero[1+i,6-i]<-" ";
		/// Escribo la ruta 
		Escribir "Reina en Posicion -> [",2+i,",",5-i,"]";
	FinPara
	
	/// Muestro el Tablero
	Para i<-1 Hasta iLong Hacer
		Para j<-1 Hasta jLong Hacer
			Escribir "[",i,",",j,"] -> ",Tablero[i,j];
		FinPara
	FinPara
	
FinProceso
