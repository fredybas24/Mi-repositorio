# Escritura de un archivo de texto
# Se usa "with open(..., 'w')" para abrir el archivo en modo escritura ('w')
with open("my_notes.txt", "w") as archivo:  # "with" cierra automaticamente el archivo después de usarlo
    # Se escriben tres líneas de notas personales en el archivo
    archivo.write("1: La musica clasica mejora la concentracion\n")
    archivo.write("2: La programacion desarrolla el pensamiento logico\n")
    archivo.write("3: Jugar ajedrez mejora la toma de decisiones\n")

# Lectura de un archivo de texto
# Se abre el archivo en modo lectura ('r')
with open("my_notes.txt", "r") as archivo:
    # Se lee el contenido línea por línea
    linea1 = archivo.readline() # Lee la primera linea
    linea2 = archivo.readline() # Lee la segunda linea
    linea3 = archivo.readline() # Lee la tercera linea

    # Se imprime cada línea sin saltos de línea extra
    print(linea1.strip())   # Imprime primera línea
    print(linea2.strip())   # Imprime segunda línea
    print(linea3.strip())   # Imprime tercera línea