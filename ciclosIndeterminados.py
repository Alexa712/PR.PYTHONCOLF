#Juego para determinar un numero aleatoreo

import random

aleatoreo = random.randrange(1,20)
numeroIngresado = int(input('Por favor ingrese el numero a adivinar del 1 al 20: '))
contadorIntentos = 0

while aleatoreo != numeroIngresado:
    print('Número ingresado en incorrecto')
    numeroIngresado = int(input('Por favor ingrese el numero a adivinar del 1 al 20: '))
    contadorIntentos +=1

print(f'Muy bien el número ingresado es: {str(numeroIngresado)}, en númrero de intentos: {str(contadorIntentos)}')
