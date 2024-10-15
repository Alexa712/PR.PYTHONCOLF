from animal import Animal

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre,4)

gato1 = Gato('Polar')

gato1.saludar()