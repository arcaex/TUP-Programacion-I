import sqlite3
conexion = sqlite3.connect('dbTest.db')
cursor = conexion.cursor()

def mostrarClientes():
    conexion = sqlite3.connect('dbTest.db')
    cursor = conexion.cursor()
    filas = cursor.execute("SELECT id_cliente,nombre,apellido, dni FROM clientes")

    for fila in filas:
        print("<id>:" + str(fila[0]) + "    <nombre>:" + fila[1] + "    <apellido>:" + fila[2] )

mostrarClientes()

id_cliente = input("Ingrese el Id de Cliente \n")

cursor.execute("DELETE FROM clientes WHERE id_cliente = " + id_cliente)
conexion.commit()
conexion.close()

mostrarClientes()

