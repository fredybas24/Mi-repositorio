temperaturas = [
    # Ciudad 1
    [
        # Semana 1
        [30, 31, 29, 28, 27, 29, 30], # Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo.
        # Semana 2
        [31, 32, 30, 29, 28, 30, 31],
        # Semana 3
        [32, 33, 31, 30, 29, 31, 32]
    ],
    # Ciudad 2
    [
        # Semana 1
        [25, 26, 24, 23, 22, 24, 25], # Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo.
        # Semana 2
        [26, 27, 25, 24, 23, 25, 26],
        # Semana 3
        [27, 28, 26, 25, 24, 26, 27]
    ],
    # Ciudad 3
    [
        # Semana 1
        [20, 22, 21, 19, 18, 20, 21], # Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo.
        # Semana 2
        [21, 23, 22, 20, 19, 21, 22],
        # Semana 3
        [22, 24, 23, 21, 20, 22, 23]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_index in range(len(temperaturas)): # Recorremos cada ciudad
    for semana_index in range(len(temperaturas[ciudad_index])): # Recorremos cada semana
        # Calculamos el promedio de temperaturas en la semana para esa ciudad
        promedio_semana = sum(temperaturas[ciudad_index][semana_index]) / len(temperaturas[ciudad_index][semana_index])
        print(f"La temperatura promedio en la Ciudad {ciudad_index + 1} de la semana {semana_index + 1}: {promedio_semana:.2f}")
    print()