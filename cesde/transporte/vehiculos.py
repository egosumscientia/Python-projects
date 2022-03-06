class Vehiculo:
    def __init__(self, motor, nroruedas, nroasientos):
        self.__motor = motor
        self.__nroruedas = nroruedas
        self.__nroasientos = nroasientos
    
    def getMotor(self):
        return self.__motor

    def setMotor(self, motor):
        self.__motor = motor

    def getRuedas(self):
        return self.__nroruedas

    def setRuedas(self, nroruedas):
        self.__nroruedas = nroruedas
    
    def getAsientos(self):
        return self.__nroasientos
    
    def setAsientos(self, nroasientos):
        self.__nroasientos = nroasientos

    def arrancar(self):
        print("El vehiculo está arrancando")

    def frenar(self):
        print("El vehículo está frenando")

    def acelerar(self):
        print("El vehiculo está acelerando")