'''
Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
'''

def cal_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros)/ len(numeros)

lista = [20,21,25,50,30,100,125]
media = cal_media(lista)
print('La media es: ', media)