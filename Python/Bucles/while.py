# El bucle while (mientras) ejecuta un fragmento de código mientras se
# cumpla una condición.

edad = 0
while edad < 18:
    edad = edad + 1
    print ("Felicidades, tienes" + str(edad))
    
salir = False
# if salir --> if salir == True
# if not salir --> if salir == False

while not salir:
    opcion = input("Ingrese Entrada \n")
    if opcion == "adios":
        salir = True
    else:
        print(opcion)

opcion = ""
while (opcion!="adios" or opcion=="seguir"):
    opcion = input("Ingrese Entrada \n")


