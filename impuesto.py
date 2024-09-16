'''
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a $59.000.000 Anuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos anuales y muestre por pantalla si el usuario tiene que tributar o no.
'''

edad = int (input('Ingrese su edad: '))
ingreso = int (input('Ingrese el total de sus ingresos anuales: $'))

if ingreso < 59000000:
    print ('Señor usuario teniendo en cuenta sus ingresos usted no debe declarar impuestos')
elif edad <= 18:
    print ('Es usted menor de edad no debe declarar impuestos')
else:
    print ('Señor usuario usted debe declarar impuestos')
