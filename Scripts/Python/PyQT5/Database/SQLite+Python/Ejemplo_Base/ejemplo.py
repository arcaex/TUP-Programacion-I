import sqlite3

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()
cursor.execute("")
conexion.commit()
rowsCursor = cursor.fetchall()

for fila in rowsCursor:
    print(fila)

conexion.close()