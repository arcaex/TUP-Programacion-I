# Primero se evalúa la condición del if. Si es cierta, se ejecuta su código y 
# se continúa ejecutando el código posterior al condicional; si no se cumple,
# se evalúa la condición del elif. Si se cumple la condición del elif
# se ejecuta su código y se continua ejecutando el código posterior al
# condicional; si no se cumple y hay más de un elif se continúa con el
# siguiente en orden de aparición. Si no se cumple la condición del if ni
# de ninguno de los elif, se ejecuta el código del else.

if numero < 0:
    print “Negativo”
elif numero > 0:
    print “Positivo”
else:
    print “Cero”
