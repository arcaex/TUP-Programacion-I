INSERT INTO Jugadores (nick,mail,clave) VALUES ("amartinez","amartinez@mail.com","Perro123")

DELETE FROM Jugadores WHERE mail = 'jgracia@mail.com'

UPDATE Jugadores SET mail='no-reply@mail.com', nick='no-reply', clave='ClaveSecreta123' WHERE id_jugador = 2

SELECT * FROM Jugadores WHERE mail='none@mail.com' 

SELECT Paises.continente,Ciudades.nombre FROM Paises,Ciudades WHERE Paises.id_pais=Ciudades.id_pais AND Paises.id_pais=8
