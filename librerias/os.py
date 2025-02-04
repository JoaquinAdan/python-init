import os

# Obtener el directorio actual
"""
cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)
"""

# Listar los archivos .txt
"""
txt_files = [f for f in os.listdir("./file") if f.endswith(".txt")]
print("Archivos txt:", txt_files)
"""

# Renombrar el archivo
"""
txt_files = [f for f in os.listdir("./file") if f.endswith(".txt")]
os.rename("./file/caperucita.txt", "./file/cuento.txt")
print("Archivo renombrado")
"""
