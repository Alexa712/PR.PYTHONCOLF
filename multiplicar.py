'''
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
'''

'''
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
'''

numero = int (input('Ingrese un número de entero del 1 al 10 para presentar la tabla de multiplicar: '))

if numero > 10:
 print ('numero no esta dentro del rango')

else:
    for i in range (1, 11):
        multiplicar = numero * i
        print ('la multiplicación del número ingresado es:' f' {str(numero)} x {i} = {multiplicar}')