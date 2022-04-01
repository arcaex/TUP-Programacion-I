Proceso Matriz_Alumnos
	Definir Alumnos Como Caracter;
	Definir iLong, jLong, i, j Como Entero;
	Dimension Alumnos[999,999];
	iLong<-0;
	jLong<-0;
	i<-0;
	j<-0;
	///[0,0][0,1][0,2]
	///[1,0][1,1][1,2]
	///[2,0][2,1][2,2]
	///[3,0][3,1][3,2]
	Escribir "Ingresar número de filas";
	Leer iLong;
	Escribir  "Ingresar número de columnas";
	Leer jLong;
	
	Para i<-0 Hasta iLong-1 Hacer
		Escribir "----------------------";
		Para j<-0 Hasta jLong-1 Hacer
			Escribir "Ingresar el Elemento [",i,",",j,"] de la Matriz";
			Leer Alumnos[i,j]; /// Matriz[fila,columna]
		FinPara
	FinPara
	Escribir "----------------------";
	Escribir "Muestra de Datos";
	Escribir "----------------------";
	Para i<-0 Hasta iLong-1 Hacer
		Escribir "----------------------";
		Para j<-0 Hasta jLong-1 Hacer
			Escribir "[",i,",",j,"] -> ",Alumnos[i,j];
		FinPara
	FinPara
FinProceso
