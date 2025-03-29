informacion_personal = {
    "nombre": "Fredy",
    "edad": 24,
    "ciudad": "Gualchan"
}

# Modificar el valor de la clave "ciuddad"
informacion_personal["ciudad"] = "Ibarra"

# Agregar la clave "profesion"
informacion_personal["profesion"] = "Ingeniería"

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal['telefono'] = "0990589465"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
