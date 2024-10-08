class Vehiculo:
    color = 'Sin color'
    puertas = 4
    llantas = 4
    marca = ''
    combustible = 0
    motor = 0
    caballos = 0
    encendido = False

    def __init__(self, color, puertas, llantas, marca, combustible, motor, caballos):
        self.color = color
        self.puertas = puertas
        self.llantas = llantas
        self.marca = marca
        self.combustible = combustible
        self.motor = motor
        self.caballos = caballos

    def arrancar (self):
        if(self.encendido != True):
            print ("Vehiculo en marcha")
            self.encendido = True
        else:
            print("Vehiculo ya se ha puesto en marcha")
        
mercedes = Vehiculo('Rojo', 5, 6, 'mercedes', 10, 3000, 50)

mercedes.arrancar