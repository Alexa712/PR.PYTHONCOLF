#Programa que valide si soy o no menor de edad.

'''
Por favor NO enviar el correo Y instalar el programa
Por favor enviar el correo O instalar el programa
'''

edad = int (input("Por favor ingresa tu edad: "))

if edad < 0:
    print ("No se permiten edades negativas")
elif edad >= 0 and edad < 18:
     print ('No tienes edad suficiente para ingresar al sistema.')
else:
     print('Puedes ingresar')

if ((edad == 21) or (edad == 30)):
     print ('Reclame su pola gratis')
elif edad == 35 or edad == 25:
     print ('pague cover')
else:
     print ('Pague cover x2')