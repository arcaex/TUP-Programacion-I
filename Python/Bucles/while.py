# El bucle while (mientras) ejecuta un fragmento de código mientras se
# cumpla una condición.

edad = 0
while edad < 18:
    edad = edad + 1
    print ("Felicidades, tienes" + str(edad))
    
salir = False
# # if salir --> if salir == True
# # if not salir --> if salir == False

while not salir:
    print(" == MENU == ")
    print("1. Sumar")
    print("2. Salir")
    opcion = input("Ingrese una Opción \n")
    if opcion == "1":
       numero1 = int(input("Ingrese un número \n")) 
       numero2 = int(input("Ingrese otro número \n"))
       suma = numero1 + numero2
       print(suma)
    elif opcion == "2":
        salir = True


