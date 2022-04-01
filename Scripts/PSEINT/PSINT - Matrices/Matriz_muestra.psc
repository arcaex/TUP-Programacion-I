Proceso Matriz_Alumnos
	Definir Alumnos Como Caracter;
	Definir iLong, jLong, i, j Como Entero;
	Dimension Alumnos[999,999];
	iLong<-3;
	jLong<-3;
	i<-0;
	j<-0;
	///[0,0][0,1][0,2]
	///[1,0][1,1][1,2]
	///[2,0][2,1][2,2]
	Alumnos[1,1]="Esteban";
	Alumnos[1,2]="Rodriguez";
	Alumnos[1,3]="erodriguez@mail.com";
	Alumnos[2,1]="Mariela";
	Alumnos[2,2]="Cristel";
	Alumnos[2,3]="cmariela@mail.com";
	Alumnos[3,1]="Fernando";
	Alumnos[3,2]="Rodriguez";
	Alumnos[3,3]="frodriguez@mail.com";
	Para i<-1 Hasta iLong Hacer
		Escribir "----------------------";
		Para j<-1 Hasta jLong Hacer
			Escribir Alumnos[i,j];
			Escribir "Valor de i -> ",i;
			Escribir  "Valor de j -> ",j;
		FinPara
	FinPara
FinProceso
