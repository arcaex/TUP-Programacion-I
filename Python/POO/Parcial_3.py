# Como gran lector necesito un software que me permita ir registrando los libros que 
# voy leyendo y contabilizar las horas de lectura que hice con cada uno. Para ello 
# necesito poder :

# Cargar libros con sus datos : Nombre, Año, Editorial, Autor , Cantidad de Páginas. [X]

# Cargar géneros para englobar varios libros similares, lo único que debería 
# ingresar sería : Nombre del Género [X]

# Permitirme agregar los libros a un género específico [X]

# Cargar las horas de lectura de cada uno de esos libros.  [X]

# Listar de mayor a menor cuáles fueron los géneros que más demoré en leer y los que menos.
# Cantidad de Horas del género es mayor <---
# Sumar las Horas leídas de cada libro del género <-- 20 [X]

listadoLibros = []
listadoBibliotecas = []
puntajeGenero = []

class Libro():
    def __init__(self,nombre,anio,editorial,autor,cantidadPaginas):
        self.nombre=nombre
        self.anio=anio
        self.editorial=editorial
        self.autor=autor
        self.cantidadPaginas = cantidadPaginas
        self.horasLeido = 0

class Biblioteca():
    def __init__(self,genero):
        self.genero = genero
        self.listaLibros = []
    
    def agregarLibro(self,LibroP):
        self.listaLibros.append(LibroP)

    def sumarHoras(self):
        acumulador = 0
        for Libro in self.listaLibros:
            acumulador = acumulador + Libro.horasLeido
        return acumulador

def listar(Tipo):
    i = 1
    if Tipo=="Libros":
        for Libro in listadoLibros:
            print(str(i)+" - "+Libro.nombre)
            i=i+1
    elif Tipo=="Bibliotecas":
        for Biblioteca in listadoBibliotecas:
            print(str(i)+" - "+Biblioteca.genero)
            i=i+1


menu = '''### MENÚ ###
- 1 Agregar Libro 
- 2 Agregar Biblioteca
- 3 Agregar Libro a Biblioteca
- 4 Cargar Horas de Lectura
- 5 Más Leidos
- 6 Salir'''

opcion = True

while opcion == True :
    print(menu)
    op = int (input("Ingrese una Opción\n"))
    if op == 1:
        nombre = input("nombre\n")
        anio = input("anio\n")
        editorial = input("editorial\n")
        autor = input("autor\n")
        cantidadPaginas = input("cantidad \n")
        LibroT = Libro(nombre,anio,editorial,autor,cantidadPaginas)
        listadoLibros.append(LibroT)
    elif op == 2:
        generoBiblio = input("genero\n")
        BibliotecaT = Biblioteca(generoBiblio)
        listadoBibliotecas.append(BibliotecaT)
    elif op == 3:
        listar ("Libros")
        libro = input("Seleccione un Libro \n")
        listar("Bibliotecas")
        genero = input("Seleccione un Género \n")
        listadoBibliotecas[int(genero)-1].agregarLibro(listadoLibros[int(libro)-1])
        #Estamos haciendo referencia al elemento listadoBibliotecas[0] <--- Objeto (Biblioteca)
        #Estamos haciendo referencia al elemento listadoLibros[0] <--- Objeto (Libro)
    elif op == 4:
        listar("Libros")
        libro = input("Seleccione un Libro \n")
        cantidadHoras = input("Ingrese la cantidad de Horas \n")
        listadoLibros[int(libro)-1].horasLeido = cantidadHoras
        #listadoLibros[libro-1].horasLeido = input("Ingrese la cantidad de Horas \n")
        print("")
    elif op == 5:
        #ARREGLAR PARA MIERCOLES
        for Biblioteca in listadoBibliotecas:
            puntajeGenero.append({"genero":Biblioteca.genero,"horas":Biblioteca.sumarHoras()})
        puntajeGenero.sort(key=lambda x:x["horas"], reverse= True)
        i = 0
        for puntaje in puntajeGenero:
            i=i+1
            print(str(i)+ " - "+puntaje["genero"]+" ("+puntaje["horas"]+")" )
    elif op == 6:
        opcion=False

# [Objeto1, Objeto2]
#    0         1
# Libro1 <--- Objeto (Libro)
# Libro1.anio + 20 <--- Atributo del Objeto (String)
# Libro1.horasLeido + 20 <--- Integer
# https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/

