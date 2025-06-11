import random

def crear_tablero():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return tablero


def imprimir_tablero(tablero):
    fila = 0
    while fila < 3:
        print(f"{tablero[fila][0]}|{tablero[fila][1]}|{tablero[fila][2]}")
        if fila < 2:
            print("-" * 5)
        fila += 1


def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True


def movimiento_ia(tablero):
    #fila0
    if tablero[0][0] == tablero[0][1] != " " and tablero[0][2] == " ":
        tablero[0][2] = "O"
    elif tablero[0][1] == tablero[0][2] != " " and tablero[0][0] == " ":
        tablero[0][0] = "O"
    elif tablero[0][0] == tablero[0][2] != " " and tablero[0][1] == " ":
        tablero[0][1] = "O"
    #fila1
    elif tablero[1][0] == tablero[1][1] != " " and tablero[1][2] == " ":
        tablero[1][2] = "O"
    elif tablero[1][1] == tablero[1][2] != " " and tablero[1][0] == " ":
        tablero[1][0] = "O"
    elif tablero[1][0] == tablero[1][2] != " " and tablero[1][1] == " ":
        tablero[1][1] = "O"
    #fila2
    elif tablero[2][0] == tablero[2][1] != " " and tablero[2][2] == " ":
        tablero[2][2] = "O"
    elif tablero[2][1] == tablero[2][2] != " " and tablero[2][0] == " ":
        tablero[2][0] = "O"
    elif tablero[2][0] == tablero[2][2] != " " and tablero[2][1] == " ":
        tablero[2][1] = "O"
    #diagonal1
    elif tablero[0][0] == tablero[1][1] != " " and tablero[2][2] == " ":
        tablero[2][2] = "O"
    elif tablero[1][1] == tablero[2][2] != " " and tablero[0][0] == " ":
        tablero[0][0] = "O"
    elif tablero[0][0] == tablero[2][2] != " " and tablero[1][1] == " ":
        tablero[1][1] = "O"
    #diagonal2
    elif tablero[2][0] == tablero[1][1] != " " and tablero[0][2] == " ":
        tablero[0][2] = "O"
    elif tablero[1][1] == tablero[0][2] != " " and tablero[2][0] == " ":
        tablero[2][0] = "O"
    elif tablero[2][0] == tablero[0][2] != " " and tablero[1][1] == " ":
        tablero[1][1] = "O"
    #columna0
    elif tablero[0][0] == tablero[1][0] != " " and tablero[2][0] == " ":
        tablero[2][0] = "O"
    elif tablero[1][0] == tablero[2][0] != " " and tablero[0][0] == " ":
        tablero[0][0] = "O"
    elif tablero[0][0] == tablero[2][0] != " " and tablero[1][0] == " ":
        tablero[2][1] = "O"
    #columna1
    elif tablero[0][1] == tablero[1][1] != " " and tablero[2][1] == " ":
        tablero[2][1] = "O"
    elif tablero[1][1] == tablero[2][1] != " " and tablero[0][1] == " ":
        tablero[0][1] = "O"
    elif tablero[0][1] == tablero[2][1] != " " and tablero[1][1] == " ":
        tablero[1][1] = "O"
    #columna2
    elif tablero[0][2] == tablero[1][2] != " " and tablero[2][2] == " ":
        tablero[2][2] = "O"
    elif tablero[1][2] == tablero[2][2] != " " and tablero[0][2] == " ":
        tablero[0][2] = "O"
    elif tablero[0][2] == tablero[2][2] != " " and tablero[1][2] == " ":
        tablero[1][2] = "O"
    else:
        casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
        if casillas_vacias:
            fila, columna = random.choice(casillas_vacias)
            tablero[fila][columna] = "O"



def juego_completo(victorias_x, victorias_y):
    tablero = crear_tablero()
    jugador_actual = "X"
    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        if jugador_actual == "X":
            movimiento_jugador(tablero, jugador_actual)
        else:
            movimiento_ia(tablero)
        if hay_ganador(tablero):
            print(f"¡{jugador_actual} ha ganado!")
            if jugador_actual == "X":
                victorias_x += 1
            elif jugador_actual == "O":
                victorias_y += 1
            break
        if tablero_lleno(tablero):
            print("¡Empate!")
            break
        if jugador_actual == "O":
            jugador_actual = "X"
        else:
            jugador_actual = "O"
    return victorias_x, victorias_y

partidas = 0
victorias_x = 0
victorias_y = 0

while partidas < 3:
    victorias_x, victorias_y = juego_completo(victorias_x, victorias_y)
    print(f"X lleva {victorias_x} victorias y O lleva {victorias_y} victorias")
    partidas = partidas + 1