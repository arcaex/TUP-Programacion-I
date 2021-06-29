# Crear un archivo
# output = open("salida.txt","w")
# output.write("Estoy Escribiendo algo")
# Cerrar el Archivo
# output.close()

# output = open("salida.txt","a")
# output.write("\n Estoy Escribiendo algo más")
# Cerrar el Archivo
# output.close()

# print(data)

# entrada = input("Ingresar Valor \n")
# output = open("salida.txt","a")
# output.write("\n El usuario ingreso " + entrada)
# Cerrar el Archivo
# output.close()

# Leer un archivo
# with open('./salida.txt', 'r') as file:
#     data = []
#     data = file.read().split("\n")
# print(data)
# resultSplit = []
# for element in data:
#     splitted = element.split("|")
#     print(splitted[0])
#     print(splitted[1])
#     print(splitted[2])
#     resultSplit.append(splitted)
# print(resultSplit)

operacion = "suma"
print(operacion[0])

valor1 = input("Ingrese un valor \n")
valor2 = input("Ingrese el segundo valor \n")
resultado = int(valor1) + int(valor2)
output = open("resultados.utn","a")
output.write( operacion + "|" + valor1 + "|" + valor2 + "|" + str(resultado) + "\n")
print("El resultado de la suma es ", resultado )
output.close()


# Leer un archivo
with open('./resultados.utn', 'r') as file:
    data = []
    data = file.read().split("\n")

data.pop()

print(data)

resultSplit = []

for element in data:
    splitted = element.split("|")
    resultSplit.append(splitted)

print(resultSplit)

for resultado in resultSplit:
    print("Operacion ->" + resultado[0] + ", Valor 1 ->" + resultado[1] + ", Valor 2 ->" + resultado[2] + ", Resultado -> " + resultado[3]) 

