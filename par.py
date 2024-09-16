'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

numero = int (input ('Ingrese un número un numero entero: '))

if numero % 2 == 0:
    print (numero, 'Numero es par')
else:
    print (numero, 'Numero es impar')
    