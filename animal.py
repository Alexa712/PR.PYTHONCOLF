class Animal:
    nombre = ''
    patas = 0

    def __init__ (self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def saludar(self):
        print('Hola soy' + self.nombre)

