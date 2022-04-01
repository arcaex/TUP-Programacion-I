#KEY-VALUE o Clave Valor
diccionario = {
'nombre' : 'Carlos', 
'edad' : 22, 
'cursos': ['Python','Django','JavaScript'] }

# Recorrer el Diccionario
for key in diccionario:
  print (key, ":", diccionario[key])

print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])

print(diccionario['cursos'][0])
print(diccionario['cursos'][1])
print(diccionario['cursos'][2])

for elem in diccionario['cursos']:
  print(elem)
