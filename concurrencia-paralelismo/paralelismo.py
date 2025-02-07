import multiprocessing


# Función que calcule el cuadrado de un número
def calculate_square(n):
    return n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Crear un pool
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)

    print(f"Resultados: {results}")


# ________________________________________________________________________
# |                       |                       |                       |
# |       CONCEPTO        |     CONCURRENCIA      |      PARALELISMO      |
# |_______________________|_______________________|_______________________|
# |                       |  Manejo de múltiples  | Ejecución simultánea  |
# |       Definición      | tareas progresivamente|  de múltiples tareas  |
# |_______________________|_______________________|_______________________|
# |                       |   Operaciones I/O     |  Tareas que requieran |
# |      Usos ideales     |    (Espera de red,    |   mucho cálculo       |
# |                       | Escritura de archivos)| o tiempo de ejecución |
# |_______________________|_______________________|_______________________|
# |                       |                       |                       |
# |     Implementación    |  threading, asyncio   |    multiprocessing    |
# |_______________________|_______________________|_______________________|
