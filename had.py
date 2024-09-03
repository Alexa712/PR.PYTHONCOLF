#Realizar un programa que conste de una clase llamada Estudiante, 
    #que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos 
    #y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. 
#1. Clase constructor para recibir los nombre y la nota
#2. Definir un metodo

class estudiante:
    print ('Ingresa nombre del estudiante')
    nombre = input()
    print ('Ingresa nota del estudiante entre 0 y 5')
    nota = input()
    
    def __init__(self,nombre, nota):
        self.nombre=nombre
        self.nota = nota
        def resultado(self):
        if self.nota >=3:
            print ('Aprobo')
        else:
            print('Perdio')
        
            print ('El estudiente' + self.nombre + 'obtuvo como nota final' + self.nota)

Alumno=estudiante 
Alumno.resultado()
      