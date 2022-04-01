class Peon:
    def __init__(self,posicionX,posicionY,color):
        self.posicionX=posicionX
        self.posicionY=posicionY
        self.color=color
    
    def __del__(self):
        print("La pieza se fue")
    
    def comer(self):
        if(self.color=="Negro"):
            self.posicionX=self.posicionX+1
            self.posicionY=self.posicionY+1
        else:
            self.posicionX=self.posicionX-1
            self.posicionY=self.posicionY-1
    
    def avanzar(self):
        if(self.color=="Negro"):
            self.posicionY=self.posicionY+1
        else:
            self.posicionY=self.posicionY-1

pieza1=Peon(1,1,"Negro")
pieza2=Peon(1,2,"Blanco")

pieza1.avanzar()
pieza1.comer()

pieza2.avanzar()
pieza2.comer()

print(pieza1.posicionX,",",pieza1.posicionY)

print(pieza2.posicionX,",",pieza2.posicionY)

del pieza1
del pieza2






