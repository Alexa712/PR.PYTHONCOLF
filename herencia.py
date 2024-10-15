class Animal:
    nombre = ''
    patas = 0

    def __init__ (self, nombre, patas):
        self.nombre = nombre
        self.pata = patas

    def saludar(self):
        print('Hola soy ' + self.nombre)


class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre,4)

gato1 = Gato('Polar')

gato1.saludar()