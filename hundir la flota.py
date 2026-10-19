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


imprimir_tablero_jugador(crear_tablero(6))