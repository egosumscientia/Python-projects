import time
import heapq

#Parametros del elevador
MAX_PISO = 5
MIN_PISO = 1
MAX_PESO = 400 #Kg

elevador = {
    "piso_actual":1,
    "peso_actual":0,
    "puertas_abiertas":False,
    "llamadas":[]  #Usaremos una lista como cola de prioridad
}

def abrir_puertas():
    elevador["puertas_abiertas"] = True
    print("Puertas abiertas.")
    time.sleep(1)

def cerrar_puertas():
    elevador["puertas_abiertas"] = False
    print("Puertas cerradas")
    time.sleep(1)

def mover_elevador(piso_destino):
    while elevador["piso_actual"] != piso_destino:
        if elevador["piso_actual"] < piso_destino:
            elevador["piso_actual"] += 1
        else:
            elevador["piso_actual"] -= 1
        print(f"Elevador en el piso {elevador['piso_actual']}")
        time.sleep(1)

    abrir_puertas()
    print(f"Elevador ha llegado al piso {piso_destino}")
    cerrar_puertas()

def llamar_elevador(piso_origen):
    if MIN_PISO <= piso_origen <= MAX_PISO:
        heapq.heappush(elevador["llamadas"], (abs(elevador["piso_actual"] - piso_origen), piso_origen))
        print(f"Elevador llamado al piso {piso_origen}")
    else:
        print("Piso no valido")


def procesar_llamadas():
    while elevador["llamadas"]:
        _,piso_destino = heapq.heappop((elevador["llamadas"]))
        mover_elevador(piso_destino)

#simulaci[on de llamadas al elevador
llamar_elevador(3)
llamar_elevador(5)
llamar_elevador(2)
procesar_llamadas()












