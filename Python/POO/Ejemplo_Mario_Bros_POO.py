
#DEFINICION DE UNA CLASE
class Mario_Bros:
    #self se refiere al objetivo mismo (A si mismo)
    #Para llamar a cada uno de los metodos o el instanciamiento de un objeto debemos pasar
    #por parametro self.
    # Construccion o creacion del objeto __init__ (Constructor)
    # Destruccion del objeto __del__ (Destructor)
    # perro.raza
    # perro.color
    #INSTANCIACION - Estado inicial del Objeto
    def __init__(self, color, letra, posicionX, posicionY):
        #Si queremos modificar el estado de un objeto o llamar a un metodo propio de si mismo deberemos
        #hacer uso del self.atributo o self.metodo
        self.color = color
        self.letra = letra
        self.posicionX = posicionX
        self.posicionY = posicionY
        print("Se creo un Mario Bros de Color:"+color+" y con la Letra: "+letra)


#Instanciar un objeto mediante la Clase 
personaje = Mario_Bros("rojo","M",0,0)
personaje2 = Mario_Bros("verde","L",1,1)
personaje3 = Mario_Bros("lila","W",2,2)

print(personaje.color)
print(personaje2.color)
print(personaje3.color)

