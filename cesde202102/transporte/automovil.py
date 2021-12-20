#from transporte.automovil import vehiculos

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


class Automovil(Vehiculo):
    def __init__(self, motor, nroruedas, nroasientos, guantera, nropuertas):
        super().__init__(motor, nroruedas, nroasientos)
        self.__guantera = guantera
        self.__nropuertas = nropuertas
        
    def getGuantera(self):
        return self.__guantera
    
    def setGuantera(self, guantera):
        self.__guantera = guantera
    
    def getPuertas(self):
        return self.__nropuertas
    
    def setPuertas(self, nropuertas):
        self.__nropuertas = nropuertas

    def reversar(self):
        return "Vehículo en reversa..."

v1 = Vehiculo("6000cc", 4, 4)
print(v1.getAsientos())
print(v1.getMotor())
print(v1.getRuedas())

v2 = Automovil("4500cc",4,4,True,5)
print(v2.getAsientos())
print(v2.getMotor())
print(v2.setMotor("5450cc"))
print(v2.getMotor())
print(v2.reversar())
