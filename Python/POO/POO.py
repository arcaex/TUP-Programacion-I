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
    def __init__(self, combustible, ventanas, puertas, color, material):
        self.combustible = combustible
        self.ventanas = ventanas
        self.puertas = puertas
        self.color = color
        self.material = material
        self.posicion = coordenadas(0,0,0)
        self.encendido = False

    def encendido(self,estado):
        self.encendido = estado
    
    def desplazarY(self,posY):
        self.posicion.posY = posY

    def desplazarZ(self,posZ):
        self.posicion.posZ = posZ

    def desplazarX(self,posX):
        self.posicion.posX = posX

class avion(vehiculo):
    def __init__(self, combustible, ventanas, puertas, color, material):

        
        


class automovil:
    def __init__(self,color,cantidadPuertas, marca, modelo, tipoCombustible,nombre,apellido, edad):
        self.color = color
        self.cantidadPuertas = cantidadPuertas
        self.marca = marca
        self.modelo = modelo
        self.tipoCombustible = tipoCombustible
        self.km = 0
        self.posicion_x = 0
        self.conductor = conductor(nombre, apellido, edad)

    def __del__(self):
        print("Se destruyo el objeto ",vars(self))

    def aumentarKm(self,cantidad):
        self.km = self.km + cantidad

    def avanzar(self):
        self.posicion_x = self.posicion_x + 1
        self.aumentarKm(10)

    def caracteristicas(self):
        return vars(self)

    def verConductor(self):
        return vars(self.conductor)

mi_auto = automovil("rojo","3","Ford","2019","Nafta","Jorge","Garcia", "33")
el_auto = automovil("verde","5","Fiat","2015","Gasoil","Pedro","Marmol","50")

print(mi_auto.tipoCombustible)

print(mi_auto.caracteristicas())
print(el_auto.caracteristicas())

mi_auto.aumentarKm(20)
el_auto.aumentarKm(40)

print(mi_auto.caracteristicas())
print(el_auto.caracteristicas())

mi_auto.avanzar()
el_auto.avanzar()

print(mi_auto.caracteristicas())
print(el_auto.caracteristicas())

print(mi_auto.verConductor())
print(el_auto.verConductor())

del mi_auto
del el_auto