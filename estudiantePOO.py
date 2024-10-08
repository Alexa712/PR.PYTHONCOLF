'''
Hacer este ejercicio python con POO para la proxima clase.
Ejercicio 1:
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos 
el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''
class Estudiante:
    nombre = ''
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def informacion (self):
        print(f'Nombre: {self.nombre}')
        print(f'Nota: {self.nota}')

    def calificar (self):
        if 3 <= self.nota <= 5:
            return f'{self.nombre} Ha aprobado.'
        elif 0  <= self.nota < 3:
            return f'{self.nombre} No ha aprobado.'
        else:
            return 'Ingrese una nota valida'

nombre = input ('Ingresa tu nombre: ')
nota = float(input('Ingresa tu nota (0 a 5): '))

estudiante = Estudiante(nombre,nota)
estudiante.informacion()
print(estudiante.calificar())



