UPDATE clientes SET fecha_alta='01/11/2021'
UPDATE clientes SET nombre='Jorge' WHERE nombre='jorge'
UPDATE clientes SET nombre='Jorge', email='jorge@mail.com', apellido='Gracia' WHERE id_cliente = 1
UPDATE clientes SET fecha_alta='01-11-2021' WHERE fecha_alta='01/11/2021'
UPDATE clientes SET nombre=upper(nombre), apellido=upper(apellido) WHERE id_cliente = 1
UPDATE clientes SET nombre=upper(nombre), apellido=upper(apellido)
INSERT clientes (nombre,apellido,dni) VALUES(lower() )