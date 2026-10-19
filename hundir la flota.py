import random

def crear_tablero(n):
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(".")
        tablero.append(fila)
    return tablero


def imprimir_tablero_jugador(tablero):
    encabezado = "  "
    for i in range(len(tablero)):
        encabezado += str(i) + " "
    print(encabezado)
    for i in range(len(tablero)):
        fila = tablero[i]
        texto_fila = str(i) + " "
        for celda in fila:
            texto_fila += celda + " "
        print(texto_fila)

def crear_barcos(tablero):
    barcos = [1,1,2,2,3,4]
    tamano = len(barcos)
    for barco in barcos:
        colocado = False
        while not colocado:
            f = random.randint(0, tamano - 1)
            c = random.randint(0, tamano - 1)
            if f + barco <= tamano:
                libre = True
                for i in range(barco):
                    if tablero[f+i][c] != "~":
                        libre = False
                if libre:
                    for i in range(barco):
                        tablero[f+i][c] = "B"
                        colocado = True



