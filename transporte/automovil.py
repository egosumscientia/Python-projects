from transporte.automovil import vehiculos

class Automovil(Vehiculo):
    def __init__(self, motor, nroruedas, nroasientos, guantera, nropuertas):
        super().__init__(self, motor, nroruedas, nropuertas)
        self.__guantera = guantera
        self.__nropuertas

    def getGuantera(self):
        return self.__guantera
    
    def setGuantera(self):
        self.__guantera = guantera
    
    def getPuertas(self):
        return self.__nropuertas
    
    def setPuertas(self):
        self.__guantera = nropuertas

    def reversar(self):
        return "Vehículo en reversa..."
