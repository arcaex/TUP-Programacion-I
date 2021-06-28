#Definición de la Función
def print_mundo():
    print("Hola Mundo")

def print_parametro(entrada):
    print(entrada)

def mi_funcion(param1, param2):
    suma = int(param1) + int(param2)
    print(str(suma))

def suma(param1,param2):
    return param1+param2

def mi_funcion_retorno(param1, param2):
    suma = int(param1) + int(param2)
    return suma

# #Llamada a la Función
# mi_funcion(1,2)
print_mundo()
print_parametro("Hola")
mi_funcion(1,2)
sumaRetorno = mi_funcion_retorno(3,4)
print(sumaRetorno)