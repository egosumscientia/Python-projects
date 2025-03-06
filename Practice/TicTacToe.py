
def inicializar_tablero():
    """Crea un tablero vacio de 3x3"""
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola"""
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

def es_movimiento_valido(tablero, fila, col):
    """Verifica si la casilla esta vacia"""
    return tablero[fila][col] == ' '

def realizar_movimiento(tablero, fila, col, jugador):
    """Coloca la marca del jugador en el tablero"""
    tablero[fila][col] = jugador

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador ha ganado"""
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True

    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True


    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    """Verifica si el tablero esta lleno"""
    return all(celda != ' ' for fila in tablero for celda in fila)

def jugar_tic_tac_toe():
    """Ejecuta el juego"""
    tablero = inicializar_tablero()
    jugador_actual = 'X'

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, ingresa la fila (0-2): "))
        col = int(input(f"Jugador {jugador_actual}, ingresa la columna (0-2): "))

        if es_movimiento_valido(tablero, fila, col):
            realizar_movimiento(tablero, fila, col, jugador_actual)
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"Jugador {jugador_actual} ha ganado!")
                break
            elif tablero_lleno(tablero):
                imprimir_tablero()
                print("Empate!")
                break
            jugador_actual = 'O' if jugador_actual == 'X' else 'X'

        else:
            print("Movimiento no permitido, intenta de nuevo.")

jugar_tic_tac_toe()
























