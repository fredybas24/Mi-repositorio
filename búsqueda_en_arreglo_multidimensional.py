matriz = [
    [5,10,15],
    [20,25,30],
    [35,40,45],
]

def buscar_valor(matriz, valor):
    for fila in range(len(matriz)): # Recorremos cada fila de la matriz
        for columna in range(len(matriz[fila])): # Recorremos cada columna de la fila
            if matriz[fila][columna] == valor: # Comparamos si el número actual es el que buscamos
                return fila, columna # Si lo encontramos, devolvemos la posición (fila, columna)
    return None # Si no lo encontramos, devolvemos None (signfica que no está en la matriz)

valor_buscado = 25
resultado = buscar_valor(matriz, valor_buscado)

# Mostramos un mensaje que indique si el valor se encontró o no, y muestramos su posición (si el valor se encotró).
if resultado:
    print(f"El elemento {valor_buscado} se encuentra en la posición {resultado}")
else:
    print(f"El elemento {valor_buscado} no se encuentra en la matriz")