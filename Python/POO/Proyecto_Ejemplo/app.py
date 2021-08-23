from clases.cancion import Cancion
from clases.lista import Lista

menu = '''### MENÚ ###
- 1 Agregar Canción
- 2 Crear una Lista
- 3 Agregar Canción a Lista
- 4 Quitar Canción de Lista
- 5 Buscar
- 6 Salir'''

opcion = True
mis_canciones = []
mis_listas = []

def add_lista():
    nombre = input("Nombre de la Lista\n")
    mis_listas.append(Lista(nombre))
    print("Se creó la Lista "+mis_listas[len(mis_listas)-1].nombre)
    #Devuelvo el índice de lo insertado
    return len(mis_listas)-1

while opcion == True :
    print(menu)
    op = int (input("Ingrese una opcion\n"))
    if op == 1:
        titulo = input("Título\n")
        interprete = input("Interprete\n")
        duracion = input("Duración \n")
        genero = input("Género \n")
        anio = input("Año \n")
        sello = input("Sello \n")
        album = input("Album \n")
        cancion = Cancion(titulo,interprete,float(duracion),genero,anio,sello,album)
        mis_canciones.append(cancion)
        print(mis_canciones[len(mis_canciones)-1])
    elif op == 2:
        add_lista()
    elif op == 3:
        print("LISTA DE CANCIONES \n")
        for cancion in mis_canciones:
            print(str(mis_canciones.index(cancion))+"-"+cancion.titulo+"\n")
        print("Ingrese las canciones que quiera agregar a una lista \n")
        print("(Separadas por comas)\n")
        canciones = input()
        canciones_split = canciones.split(",")
        #Damos la opción de agregar una lista nueva o utilizar las cargadas
        nueva_lista = input("¿Quiere cargar una lista nueva? S/N \n")
        if(nueva_lista=="S"):
            listaIndex = add_lista()
        else:
            print("SELECCIONE UNA LISTA \n")
            for lista in mis_listas:
                print(str(mis_listas.index(lista))+"-"+lista.nombre+"\n")
                listaIndex = input()
        #Agregar las canciones del split a la lista ingresada o seleccionada
        for cancionIndex in canciones_split:
            mis_listas[int(listaIndex)].agregar(mis_canciones[int(cancionIndex)])
        #Imprimo las canciones agregadas a la lista
        print(mis_listas[int(listaIndex)].listado_canciones)
    elif op == 4:
        print("")
    elif op == 5:
        print("")
    elif op == 6:
        opcion=False
