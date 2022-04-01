# Clase: Cancion
# Parametros: titulo, interprete, duracion en segundos, estilo musical
# Metodos:
#   resumen: devuelve titulo e interprete (formato resumido)
#   __str__: devuelve todos los parametros (formato completo)
#   Class: Canciones
#   Parametro: listado de canciones
#   Metodos:
#   listar_por_estilo: Muestra todas las canciones de un estilo (formato resumido)
#   listar_por_interprete: Muestra todas las canciones de un interprete(formato resumido)
#   Agregar: agrega una cancion (OK)
#   listar_todas: Muestra todas las canciones (formato completo) (OK)
#   quitar: quitar una cancion por titulo e interprete (OK)

import datetime

class Lista:
    def __init__(self):
        self.listado_canciones = []
    
    def agregar(self,song):
        if type(song) == Cancion:
            self.listado_canciones.append(song)
            print("Se agregó la canción : "+song.titulo)
        else:
            print("No es una canción")
    
    def listar_todas(self):
        for cancion in self.listado_canciones:
            print(cancion)

    def quitar(self,titulo,interprete):
        for cancion in self.listado_canciones:
            if(cancion.titulo==titulo and cancion.interprete==interprete):
                self.listado_canciones.remove(cancion)
    
    def listar_por_interprete(self,interprete):
        for cancion in self.listado_canciones:
            if(cancion.interprete==interprete):
                print(cancion.resumen())
    
    def listar_por_interprete_lista(self,interprete):
        retornoLista = []
        for cancion in self.listado_canciones:
            if(cancion.interprete==interprete):
                retornoLista.append(cancion.resumen())
        return retornoLista
    
    def listar_por_estilo(self,genero):
        for cancion in self.listado_canciones:
            if(type(cancion.genero)==list):
                if(cancion.genero.count(genero)>0):
                    print(cancion.resumen())
            else:
                if(cancion.genero.find(genero)!=-1 and type(cancion.genero)==str):
                    print(cancion.resumen())
            
class Cancion:
    def __init__(self,titulo,interprete,duracion,genero,anio,sello,album):
        self.titulo = titulo
        self.interprete = interprete
        self.duracion = duracion
        self.genero = genero
        self.anio = anio
        self.sello = sello
        self.album = album
    
    def resumen(self):
        return (self.titulo+" - "+self.interprete)

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(self.titulo, self.interprete, datetime.timedelta(minutes=self.duracion), self.genero , self.anio, self.sello, self.album)

#cancion1 = Cancion("Enjoy the Silence","Depeche Mode", 2.4, ["Rock Alternativo","Dance Pop","Electro Pop","Synth Pop"],1990,"Mute Records", "Violator")
#cancion2 = Cancion("De Música Ligera","Soda Stereo", 3.22, "Rock Alternativo",1990,"CBS Discos", "Canción Animal")
#cancion3 = Cancion("Canción Animal","Soda Stereo", 2.5, ["Rock Alternativo","Power Pop"],1990,"CBS Discos", "Canción Animal")

#lista = Lista()
#lista.agregar(cancion1)
#lista.agregar(cancion2)
#lista.agregar(cancion3)
#lista.listar_por_estilo("Rock Alternativo")
#lista.quitar("Enjoy the Silence","Depeche Mode")
#lista.listar_por_interprete("Soda Stereo")
#lista.listar_todas()

opcion=0
while(opcion==0):
    print("1. Agregar Canción \n 2.Crear Lista \n 3. Buscar \n 4. Quitar \n 0. Salir")
