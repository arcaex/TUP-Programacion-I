SELECT * FROM clientes
SELECT dni FROM clientes
SELECT apellido, nombre, dni FROM clientes
SELECT apellido || ' ' || nombre, dni FROM clientes
SELECT apellido || ' ' || nombre as cliente, dni FROM clientes
SELECT * FROM clientes WHERE dni = 33443334
SELECT * FROM clientes WHERE nombre = 'maria' AND dni = 4662334
SELECT id_cliente, email FROM clientes WHERE nombre = 'maria' AND dni = 4662334

SELECT * FROM clientes WHERE nombre = 'maria' OR nombre= 'jorge'
SELECT * FROM clientes WHERE dni > 4662334
SELECT * FROM clientes WHERE dni < 4662334
SELECT * FROM clientes WHERE dni <= 4662334
SELECT * FROM clientes WHERE dni >= 4662334
SELECT * FROM clientes WHERE dni <> 4662334

SELECT COUNT(*) as total FROM clientes 
SELECT COUNT(*) as total FROM clientes WHERE nombre="carlos"
SELECT dni FROM clientes GROUP BY dni
SELECT nombre FROM clientes GROUP BY nombre
SELECT * FROM clientes LIMIT 1
SELECT * FROM clientes ORDER BY nombre ASC, apellido ASC
SELECT * FROM clientes ORDER BY id_cliente ASC

SELECT (dni+edad) as resultado FROM clientes 