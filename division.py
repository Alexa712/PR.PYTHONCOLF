''''
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

numero_1 = int (input ('Ingrese un numero: '))
numero_2 = int (input ('Ingrese un segundo numero: '))

if numero_2 <= 0:
    print ('El divisor no puede ser cero')

else:
    resultado = numero_1//numero_2 
    print ('Resultado al dividir', numero_1, 'entre', numero_2, 'es', resultado)
