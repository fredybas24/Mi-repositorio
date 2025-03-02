matriz = [
    [5,10,3],
    [8,4,2],
    [7,9,6]
]

def bubble_sort_matriz(matriz):
    filas = len(matriz) # Obtiene el número de filas
    columnas = len(matriz[0]) # Obtiene el número de columnas

    # Convertimos la matriz en una lista unidimensional
    lista = [matriz[i][j] for i in range(filas) for j in range(columnas)]

    # Aplicamos Bubble Sort a la lista generada
    n = len(lista) # Longitud total de la lista
    for i in range(n): # Recorremos la lista varias veces (n veces)
        for j in range(0,n - i - 1): # Comparación de pares de elementos
            if lista[j] > lista[j+1]: # Intercambiamos si el anterior es mayor que el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]

    # Reconstruimos la matriz ordenada
    matriz_ordenada = []
    for i in range(filas):
        fila = lista[i * columnas:(i + 1) * columnas] # Extraemos segmentos de la lista
        matriz_ordenada.append(fila)

    return matriz_ordenada # Retornamos la matriz ordenada

print("matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = bubble_sort_matriz(matriz)

print("\nMatriz ordenada:")
for fila in matriz_ordenada:
    print(fila)
