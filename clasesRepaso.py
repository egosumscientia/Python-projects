from transporte.vehiculos import Vehiculo
from transporte.automovil import *

vehiculo1 = Vehiculo("5500cc", 4, 5)

print(vehiculo1.getAsientos())

auto1 = Automovil("6000cc", 4, 5, 1, 5)
print(auto1.getMotor())
