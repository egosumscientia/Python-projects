##### VERSION POO #####
from Practice.Classes_examples import cuenta


class Usuario:
    """Clase que representa a un usuario del ATM"""

    def __init__(self, cuenta, pin, saldo=0):
        self.cuenta = cuenta
        self.pin = pin
        self.saldo = saldo

    def autenticar(self, pin):
        return self.pin == pin

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")

    def depositar(self, cantidad):
        if cantidad>0:
            self.saldo+=cantidad
            print(f"Deposito exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Cantidad no valida")

    def retirar(self, cantidad):
        if 0<cantidad<=self.saldo:
            self.saldo-=cantidad
            print(f"REtiro exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes o cantidad no valida")

class Cajero:

    def __init__(self):
        self.usuarios = {
            '12345': Usuario('12345','1111',1000),
            '67890': Usuario('67890', '2222', 500)
        }

    def ejecutar(self):

        cuenta=input("Ingrese su numero de cuenta: ")
        pin=input("Ingrese su PIN: ")

        usuario = self.usuarios.get(cuenta)
        if not usuario or not usuario.autenticar(pin):
            print("Autenticacion fallida")
            return

        while True:
            print("\n--- CAJERO AUTOMÁTICO ---")
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                usuario.consultar_saldo()
            elif opcion == '2':
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                usuario.depositar(cantidad)
            elif opcion == '3':
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                usuario.retirar(cantidad)
            elif opcion == '4':
                print("Gracias por usar el cajero automático.")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    cajero = Cajero()
    cajero.ejecutar()


