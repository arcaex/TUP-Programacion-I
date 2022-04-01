import sqlite3

conexion = sqlite3.connect('dbTest.db')
cursor = conexion.cursor()

nombre = input("Ingrese Nombre \n")
apellido = input("Ingrese Apellido \n")
dni = input("Ingrese DNI \n")

cursor.execute("INSERT INTO clientes(nombre,apellido,dni) VALUES ('"+nombre+"','"+apellido+"',"+dni+")")

conexion.commit()

conexion.close()


