import datetime

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