class conductor:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class coordenadas:
    def __init__(self,x,y,z):
        self.posX = x
        self.posY = y
        self.posZ = z

class vehiculo:
    def __init__(self, combustible, ventanas, puertas, color, material,capacidad):
        self.combustible = combustible
        self.ventanas = ventanas
        self.puertas = puertas
        self.color = color
        self.material = material
        self.posicion = coordenadas(0,0,0)
        self.encendido = False
        self.capacidad = capacidad
        self.velocidad = 0

    def encender(self,enc):
        self.encendido = enc
    
    def desplazarY(self,posY):
        self.posicion.posY = posY

    def desplazarZ(self,posZ):
        self.posicion.posZ = posZ

    def desplazarX(self,posX):
        self.posicion.posX = posX

class avion(vehiculo):
    def __init__(self, combustible, ventanas, puertas, color, material, mecanismo, tipo, alturaMax, brujula):
        self.mecanismo = mecanismo
        self.tipo = tipo
        self.alturaMax = alturaMax
        self.pilotoAutomatico = False
        self.brujula = brujula
    
    def encenderPiloto(self, estado):
        self.pilotoAutomatico = estado

    def checkAlerta(self):
        if(self.posicion.posY > self.alturaMax):
            print("Alerta! Altura máxima Alcanzada")
        else:
            print("Sin problemas")

    def despegar(self):
        self.desplazarY(10000)
    
    def aterrizar(self):
        self.desplazarY(0)

Boing = avion("Jet A-1",40,10,"Blanco", "Aleación de Alta Resistencia 7075", "Turbina","Pasajero",9000,True)

Boing.encender(True)
Boing.despegar()
Boing.pilotoAutomatico(True)
print(vars(Boing))
Boing.checkAlerta()
Boing.desplazarY(5000)
Boing.checkAlerta()
Boing.pilotoAutomatico(False)
Boing.aterrizar()
Boing.encender(False)
print(vars(Boing))

