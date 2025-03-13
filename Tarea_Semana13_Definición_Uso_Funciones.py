temperaturas = [
    # Ciudad 1
    [
        # Semana 1
        [30, 31, 29, 28, 27, 29, 30],  # Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo.
        # Semana 2
        [31, 32, 30, 29, 28, 30, 31],
        # Semana 3
        [32, 33, 31, 30, 29, 31, 32]
    ],
    # Ciudad 2
    [
        # Semana 1
        [25, 26, 24, 23, 22, 24, 25],  # Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo.
        # Semana 2
        [26, 27, 25, 24, 23, 25, 26],
        # Semana 3
        [27, 28, 26, 25, 24, 26, 27]
    ],
    # Ciudad 3
    [
        # Semana 1
        [20, 22, 21, 19, 18, 20, 21],  # Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo.
        # Semana 2
        [21, 23, 22, 20, 19, 21, 22],
        # Semana 3
        [22, 24, 23, 21, 20, 22, 23]
    ]
]


# Definimos una función para calcular el promedio de temperatura por ciudad
def temperatura_promedio(temperaturas):
    promedio_ciudad = []  # Lista para almacenar el promedio de cada ciudad

    # Iteramos sobre cada ciudad en la lista de temperaturas
    for ciudad in temperaturas:
        suma_total = 0  # Variable para almacenar la suma total de temperaturas de la ciudad
        total_dias = 0  # Variable para contar la cantidad total de días registrados en la ciudad

        # Iteramos sobre cada semana en la ciudad
        for semana in ciudad:
            suma_total += sum(semana)  # Sumamos todas las temperaturas de la semana
            total_dias += len(semana)  # Contamos cuántos días tiene la semana

        # Calculamos el promedio de la ciudad dividiendo la suma total por el total de días
        promedio_ciudad.append(suma_total / total_dias)

    return promedio_ciudad  # Retornamos la lista con los promedios de cada ciudad


# Llamamos a la función para obtener los promedios de temperatura de las ciudades
promedios_ciudades = temperatura_promedio(temperaturas)

# Imprimimos los resultados de los promedios de temperatura por ciudad
print("Temperaturas promedio por ciudad:")
for i, promedio in enumerate(promedios_ciudades, start=1):  # Usamos enumerate para obtener el índice de cada ciudad
    print(f"La temperatura promedio de la Ciudad {i}: {promedio:.2f}°C")  # Mostramos el resultado con 2 decimales
