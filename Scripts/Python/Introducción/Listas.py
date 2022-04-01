# Recorrer una lista
mylist = ['one', 'two', 'three', 'four', 'five']
list2 = [1,2,3,4]

acumulador = 0

for elem in mylist:
    print(elem)

for elem in list2:
    acumulador = acumulador + elem

print(acumulador)

# Cortar una lista
mylist = ['one', 'two', 'three', 'four', 'five']
mylistshort = mylist[1:3]
print(mylistshort)

# Insertar en una lista
mylist = [1, 2, 3, 4, 5]
mylist.insert(1,'Hello')
print(mylist)

# Agregar al final
mylist = ['one', 'two', 'three', 'four', 'five']
mylist.append("new one")
print(mylist)

# Ordenar una Lista
mylist = ['cde', 'fgh', 'abc', 'klm', 'opq']
list2 = [3, 5, 2, 4, 1]

# De Menor a Mayor
mylist.sort()

# De Mayor a Menor
list2.sort(reverse=True)

print(mylist)
print(list2)

# Índice de un elemento
mylist = ['five','one', 'two', 'three', 'four', 'five', 'two']
print(mylist.index('five'))
print(mylist[2])

# Carga de Lista
mylist = []
value = input("Ingrese un valor \n")
mylist.append(value)
print(mylist)

#2x2
mylist = [['one','two'],['three','four']]
print(mylist[0][1])
print(mylist[1][1])