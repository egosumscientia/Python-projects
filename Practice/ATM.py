##### VERSION PROCEDIMENTAL  #####
# Archivo: ATM.py #
from mypy.messages import collect_all_named_types

from Practice.Classes_examples import cuenta


def autenticar_usuario(usuarios, cuenta, pin):
    """Fxn para autenticar al usuario con su # de cta y PIN"""
    return cuenta in usuarios and usuarios[cuenta]['pin'] == pin

def consultar_saldo(usuarios, cuenta):
    print(f"Saldo actual: ${usuarios[cuenta]['saldo']}")

def depositar(usuarios, cuenta, cantidad):
    if cantidad>0:
        usuarios[cuenta]['saldo']+=cantidad
        print(f"Deposito exitoso. Saldo actual: ${usuarios[cuenta]['saldo']}")
    else:
        print("Cantidad no valida")

def retirar(usuarios, cuenta, cantidad):
    if 0<cantidad<=usuarios[cuenta]['saldo']:
        usuarios[cuenta]['saldo'] -= cantidad
        print(f"Retiro exitoso. Saldo actual: ${usuarios[cuenta]['saldo']}")
    else:
        print("Fondos insuficientes o cantidad no valida")

def menu():
    """Fxn ppal del ATM"""

    usuarios = {
        '12345':{'pin':'1111', 'saldo':1000},
        '67890':{'pin':'2222', 'saldo':500}
    }

    cuenta = input("Ingrese su numero de cuenta: ")
    pin = input("Ingrese su PIN: ")

    if not autenticar_usuario(usuarios, cuenta, pin):
        print("Autenticacion fallida")
        return

    while True:
        print("\n---CAJERO AUTOMATICO (ATM)")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Selecciones una opcion: ")

        if opcion=='1':
            consultar_saldo(usuarios, cuenta)
        elif opcion=='2':
            cantidad=float(input("Ingrese la cantidad a depositar: "))
            depositar(usuarios, cuenta, cantidad)
        elif opcion=='3':
            cantidad=float(input("Ingrese la cantida a retirar: "))
            retirar(usuarios, cuenta, cantidad)
        elif opcion=='4':
            print("Gracias por usar el ATM")
            break
        else:
            print("Opcion no valida. Intente otra vez")

if __name__ == "__main__":
    menu()

