'''
Escribir una función a la que se le pase una cadena
<nombre> y muestre por pantalla el saludo
¡hola <nombre>!
'''

def saludo(nombre):
    print(f"¡Hola, {nombre}!")

nombre = input ('Ingresa tu nombre: ')

saludo(nombre)