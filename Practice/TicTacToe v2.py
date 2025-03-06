class TicTacToe:
    def __init__(self):
        """Inicializa el tablero y el jugador actual"""
        self.tablero = [[' '  for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'

    def imprimir_tablero(self):
        """Imprime el tablero en consola"""
        for i, fila in enumerate(self.tablero):
            print('|'.join(fila))
            if i<2: #Evita imprimir la linea despues de la ultima fila
                print('-' * 5)

    def es_movimiento_valido(self, fila, col):
        """Verifica si la casilla esta vacia"""
        return self.tablero[fila][col] == ' '

    def realizar_movimiento(self, fila, col):
        """Coloca la marca del jugador en el tablero"""
        self.tablero[fila][col] = self.jugador_actual

    def verificar_ganador(self):
        """Verifica si el jugador actual ha ganado"""
        for fila in self.tablero:
            if all(celda == self.jugador_actual for celda in fila):
                return True

        for col in range(3):
            if all(self.tablero[fila][col] == self.jugador_actual for fila in range(3)):
                return True

        if all(self.tablero[i][i] == self.jugador_actual for i in range(3)) or all(self.tablero[i][2-i] == self.jugador_actual for i in range(3)):
            return True

        return False

    def tablero_lleno(self):
        """Verifica si el tablero esta lleno"""
        return all(celda != ' ' for fila in self.tablero for celda in fila)


    def cambiar_turno(self):
        """Cambia el turno al otro jugador"""
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'

    def jugar(self):
        """Ejecuta el juego"""
        while True:
            self.imprimir_tablero()
            fila = int(input(f"Jugador {self.jugador_actual}, ingresa la fila (0-2): "))
            col = int(input(f"Jugador {self.jugador_actual}, ingresa la columna (0-2): "))

            if self. es_movimiento_valido(fila, col):
                self.realizar_movimiento(fila, col)
                if self.verificar_ganador():
                    self.imprimir_tablero()
                    print(f"Jugador {self.jugador_actual} ha ganado!")
                    break
                elif self.tablero_lleno():
                    self.imprimir_tablero()
                    print("Empate!")
                    break

                self.cambiar_turno()
            else:
                print("Movimiento anulado, intenta otra vez.")

TicTacToe().jugar()




















