# Leer un archivo linea por linea
"""
with open("./file/caperucita.txt", "r") as file:
    for linea in file:
        print(linea.strip())
"""

# Leer todas las lineas en una lista
"""
with open("./file/caperucita.txt", "r") as file:
    lineas = file.readlines()
    print(lineas)
"""

# Agregar una linea al final del archivo
"""
with open("./file/caperucita.txt", "a") as file:
    file.write("\n\n Hola mundo")
"""

# Sobreescribir el archivo
"""
with open("./file/caperucita.txt", "w") as file:
    file.write("Hola mundo")
"""