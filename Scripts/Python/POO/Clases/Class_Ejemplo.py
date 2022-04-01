
#DEFINICION DE UNA CLASE
class Mario_Bros:
    #self se refiere al objetivo mismo (A si mismo)
    #Para llamar a cada uno de los metodos o el instanciamiento de un objeto debemos pasar
    #por parametro self.
    # Construccion o creacion del objeto __init__
    # Destruccion del objeto __del__
    #INSTANCIACION - Estado inicial del Objeto
    def __init__(self, color, letra, posicionX, posicionY):
        #Si queremos modificar el estado de un objeto o llamar a un metodo propio de si mismo deberemos
        #hacer uso del self.atributo o self.metodo
        self.color = color
        self.letra = letra
        self.posicionX = posicionX
        self.posicionY = posicionY
        print("Se creo un Mario Bros de Color:"+color+" y con la Letra: "+letra)

    #METODOS
    def subir(self):
        self.posicionY = self.posicionY + 1

    def bajar(self):
        self.posicionY = self.posicionY - 1
    
    def avanzar(self):
        self.posicionX = self.posicionX + 1
    
    def retroceder(self):
        self.posicionX = self.posicionX - 1

    #Metodo que espera parametros
    def teletransportar(self,posicionX,posicionY):
        print("Bzzzzz!!!!!")
        self.posicionX = posicionX
        self.posicionY = posicionY

#Instanciar un objeto mediante la Clase 
personaje = Mario_Bros("rojo","M",0,0)
personaje2 = Mario_Bros("verde","L",0,0)

#Llamar a los metodos definidos de la Clase
personaje.avanzar()
personaje.avanzar()
personaje.bajar()
personaje.subir()
personaje.retroceder()

print("Posicion en X : "+str(personaje.posicionX)+" - Posicion en Y :"+ str(personaje.posicionY))

#Llamadas a metodos que esperan parametros

personaje.teletransportar(0,0)

print("Posicion en X : "+str(personaje.posicionX)+" - Posicion en Y :"+ str(personaje.posicionY))
