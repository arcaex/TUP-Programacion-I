Proceso  Ejemplo_Ordenamiento_Array_Burbuja
	/// Defino la matriz, el auxiliar, el flag y el siguiente elemento
	Definir Edades, Auxiliar, Siguiente, F Como Entero;
	/// Defino las Variables de los índices la matriz
	Definir  i,j, iLong, jLong Como Entero;
	Dimension Edades[9999,9999];
	F<-0;
	iLong<-0;
	jLong<-0;
	/// Ingresar Cantidad de Filas y Columnas
	Escribir  "Ingresar la cantidad de filas";
	Leer iLong;
	Escribir  "Ingresar la cantidad de columnas";
	Leer jLong;
	
	Para i<-0 Hasta iLong-1 Hacer
		Escribir "----------------------";
		Para j<-0 Hasta jLong-1 Hacer
			Escribir "Ingresar la edad [",i,",",j,"] de la Matriz";
			Leer Edades[i,j];
		FinPara
	FinPara
	/// Mostramos las Edades y sus índices
	Escribir "----------------------";
	Escribir "Datos Cargados";
	Para i<-0 Hasta iLong-1 Hacer
		Escribir "----------------------";
		Para j<-0 Hasta jLong-1 Hacer
			Escribir "[",i,",",j,"] -> ",Edades[i,j];
		FinPara
	FinPara
	/// Ordenamiento Si se modifica el símbolo de la condición, cambiaría de Menor a Mayor el ordenamiento.
	Escribir "----------------------";
	Escribir "Ordenar de Mayor a Menor";
	Mientras F=0 Hacer
		F<-1;
		Para i<-0 Hasta ilong-2 Hacer
			Para j<-0 Hasta jlong-2 Hacer
				Si Edades[i,j] < Edades[i+1,j+1] Entonces
					Auxiliar <- Edades[i,j];
					Edades[i,j] <- Edades[i+1,j+1];
					Edades[i+1,j+1] <- Auxiliar;
					F<-0;
				FinSi
			FinPara
		FinPara
	FinMientras
	/// Mostramos las Edades y sus índices Ordenadas de Mayor a Menor
	Escribir "----------------------";
	Escribir "Muestra de Datos del Ordenamiento";
	Para i<-0 Hasta iLong-1 Hacer
		Escribir "----------------------";
		Para j<-0 Hasta jLong-1 Hacer
			Escribir "[",i,",",j,"] -> ",Edades[i,j];
		FinPara
	FinPara
FinProceso