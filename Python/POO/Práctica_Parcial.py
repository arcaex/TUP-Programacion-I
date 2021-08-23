import uuid
from random import randint

class Producto:
    def __init__(self,descripcion,codigoBarras,precio,proveedor):
        self.id = uuid.uuid4()
        self.descripcion = descripcion
        self.clave = randint(1,200)
        self.codigoBarras = codigoBarras
        self.precio = precio
        self.proveedor = proveedor
    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}'.format(self.id,self.descripcion,self.clave,self.codigoBarras,self.precio,self.proveedor)

class Carrito:
    def __init__(self):
        self.listadoProductos = []
        self.usuario = ""
    def cargarProducto(self,prod,cant):
        self.listadoProductos.append([prod,cant])
    def mostrarProductos(self):
        i = 1
        for Producto in self.listadoProductos:
            print(str(i) + " - " + str(Producto[0].descripcion) + "\n")
            i=i+1

class ListaProductos:
    def __init__(self):
        self.listadoProductos = []
    def cargarProducto(self,prod):
        self.listadoProductos.append(prod)
    def mostrarProductos(self):
        i = 0
        for Producto in self.listadoProductos:
            print(str(i) + " - " + str(Producto.descripcion) + "\n")
            i=i+1

# Manzana = Producto("Fruta",1231241231,120,"Moño Azul")
# Carrito1 = Carrito()
# Carrito1.cargarProducto(Manzana,2)
# print(Carrito1.listadoProductos[0][0].descripcion)
# print(Carrito1.listadoProductos[0][1])
# print(Carrito1.listadoProductos)

menu = '''### MENÚ ###
- 1 Agregar Producto
- 2 Agregar al Carrito
- 3 Salir'''

opcion = True
listadoProductosObjeto = ListaProductos()
carritoProductosObjeto = Carrito()

while opcion == True :
    print(menu)
    op = int (input("Ingrese una Opción\n"))
    if op == 1:
        descripcion = input("Descripcion\n")
        codigoBarras = int (input("Codigo de Barras\n"))
        precio = int (input("Precio\n"))
        proveedor = input("Proveedor\n")
        objetoTransitorio = Producto(descripcion, codigoBarras, precio, proveedor)
        listadoProductosObjeto.cargarProducto(objetoTransitorio)
        print("Se agrego el Producto",objetoTransitorio)
        #listadoProductosObjeto(Producto(descripcion,codigoBarras,precio,proveedor))
    elif op == 2:
        listadoProductosObjeto.mostrarProductos()
        indice = int (input("Ingrese el numero del producto\n"))
        cantidad = int (input("cantidad\n"))
        productoTransitorio = listadoProductosObjeto.listadoProductos[indice]
        carritoProductosObjeto.cargarProducto(productoTransitorio,cantidad)
        carritoProductosObjeto.mostrarProductos()
    elif op == 3:
        opcion=False

