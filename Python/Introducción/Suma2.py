from functions import suma

valor1="a"
valor2="b"

while valor1.isalpha():
    valor1 = input("Ingrese el primer valor \n")

while valor2.isalpha():
    valor2 = input("Ingrese el segundo valor \n")

suma = suma(valor1,valor2)
print("El resultado es " , suma)
print("El resultado es " + str(suma))