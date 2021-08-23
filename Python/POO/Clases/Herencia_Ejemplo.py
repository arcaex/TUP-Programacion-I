#CLASE PADRE
class Personaje:
    def __init__(self,posicionX, posicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY
    #METODOS
    def subir(self):
        self.posicionY = self.posicionY + 1

    def bajar(self):
        self.posicionY = self.posicionY - 1
    
    def avanzar(self):
        self.posicionX = self.posicionX + 1
    
    def retroceder(self):
        self.posicionX = self.posicionX - 1

    def teletransportar(self,posicionX,posicionY):
        print("Bzzzzz!!!!!")
        self.posicionX = posicionX
        self.posicionY = posicionY

#HERENCIA SOBREESCRIBIENDO METODOS
#CLASE HIJA 1
class Yoshi(Personaje):
    def __init__(self,color):
        self.color = color
        self.lengua_afuera = False
        self.huevos = 0

    def sacar_lengua(self):
        self.lengua_afuera = True
    
    def comer(self):
        self.huevos = self.huevos+1

yoshiRosa = Yoshi("Verde")
yoshiRosa.sacar_lengua()
yoshiRosa.comer()
yoshiRosa.comer()

print("Lengua es "+str(yoshiRosa.lengua_afuera))
print("Huevos:"+str(yoshiRosa.huevos))


#HERENCIA DE SUPERCLASE (ATRIBUTOS HEREDADOS Y METODOS HEREDADOS)
#CLASE HIJA 2
class Honguito(Personaje):
    def __init__(self,color,posicionX,posicionY):
        Personaje.__init__(self,posicionX,posicionY)
        self.color = color
        self.scream = False

    def gritar(self):
        self.scream = True

    def avanzar(self):
        self.posicionX=self.posicionX+4

honguitoAmarillo = Honguito("Amarillo",0,0)
honguitoAmarillo.avanzar()
honguitoAmarillo.retroceder()
honguitoAmarillo.bajar()
honguitoAmarillo.gritar()

diccionario= ["Hola","como","estas"]
diccionario.append("?")
print(diccionario)

print(honguitoAmarillo.posicionX,",",honguitoAmarillo.posicionY)