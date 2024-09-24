'''
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

contraseña = 'abc123'
password = input('Introduce una contraseña: ')
contadorIntentos = 0

while contraseña != password:
    print('Contraseña Incorrecta')
    password = input('Introduce una contraseña: ')
    contadorIntentos +=1

print(f'Muy bien ingresate la contraseña correcta, en númrero de intentos: {str(contadorIntentos)}')