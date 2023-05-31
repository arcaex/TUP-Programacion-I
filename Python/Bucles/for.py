
secuencia = ["uno", "dos", "tres"]
matriz = [
    [1, 2, 3],
    [6, 7, 8],
    [10, 11, 12]
]

for i in range(0, 3, 1):
    print(matriz[i][i])

for i in range(0, 3, 1):
    print(matriz[i][2-i])

fila = ""

for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        print(matriz[::1][::1])
        fila = fila + "[" + str(matriz[i][j]) + "]"
    print(fila)
    fila = ""
#Comentario
print(matriz[::1][::1])

for elemento in secuencia:
    print(elemento)

print("Numeros del 0 al 5")

for i in range(0, 6, 2):
    print(i)

lista = [1, 2, 4, 6]

for i in range(0, 4, 1):
    print(lista[i])

for numero in lista:
    print(numero)
