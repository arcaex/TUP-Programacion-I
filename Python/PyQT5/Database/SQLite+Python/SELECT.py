import sqlite3

conexion = sqlite3.connect('dbTest.db')
cursor = conexion.cursor()

nombre = input("Ingrese un Nombre \n")

cursor.execute("SELECT COUNT(*) as total FROM clientes WHERE nombre='"+nombre+"'")

filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.close()


