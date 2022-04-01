from clases.cancion import Cancion

class Lista:
    def __init__(self,nombre):
        self.listado_canciones = []
        self.nombre=nombre
    
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