
valor1="a"
valor2="b"

while valor1.isalpha():
    valor1 = input("Ingrese el primer valor \n")

while valor2.isalpha():
    valor2 = input("Ingrese el segundo valor \n")

suma = int(valor1) + int(valor2)
print("El resultado es " , suma)
print("El resultado es " + str(suma))