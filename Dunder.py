'''
Los metodos dunder sirven para manipular la clase y vienen incluidos en la
estructura de dados de los objetos de python
'''

class Afiliado:
    nomnre = ''
    calificacion = 0
    edad = 0

    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'Tu nombre es: {self.nombre}, tu edad: {self.edad} y tu calificación es: {self.calificacion}'
    def __add__(self,x):
        sumatoria = self.calificacion + x
        return f'Tu nota sumada con el metodo __add__ es: {sumatoria}'
    def getCalificacion(self):
        calificacion = f'Tu calificación es {self.calificacion}'
        return calificacion
    
    def setCalificacion(self,calificacion):
        self.calificacion = int (calificacion) + 1
    
daniel = Afiliado('Daniel', 18)

daniel.setCalificacion(5)

calificacionDaniel = daniel.getCalificacion()

print(daniel + 1)
