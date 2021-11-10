import sqlite3
conexion = sqlite3.connect('dbTest.db')
cursor = conexion.cursor()

def mostrarClientes():
    conexion = sqlite3.connect('dbTest.db')
    cursor = conexion.cursor()
    filas = cursor.execute("SELECT id_cliente,nombre,apellido, dni FROM clientes")
    filasDic = []
    
    for fila in filas:
        filasDic.append({
            "id_cliente": fila[0],
            "nombre": fila[1],
            "apellido": fila[2],
            "dni": fila[3]})

    for cliente in filasDic:
        print(str(cliente["id_cliente"])+" "+cliente["nombre"])
        
mostrarClientes()

id_cliente = input("Ingrese el Id de Cliente \n")
nombre = input("Ingrese Nombre \n")
apellido = input("Ingrese Apellido \n")
dni = input("Ingrese DNI \n")

cursor.execute("UPDATE clientes SET nombre='"+nombre+"', apellido='"+apellido+"', dni='"+dni+"' WHERE id_cliente = " + id_cliente)

conexion.commit()
conexion.close()

mostrarClientes()

