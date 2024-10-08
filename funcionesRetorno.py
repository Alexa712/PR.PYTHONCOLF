''' 
Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función
'''

def areaCirculo(radio):
    pi = 3.1416
    area = pi * (radio**2)
    return area

def volumenCilindro (altura, radio):
    areaCililndro = areaCirculo (radio)
    volumenCilindro = areaCililndro * altura
    return volumenCilindro


cilindro = volumenCilindro (10,5)

print(cilindro)