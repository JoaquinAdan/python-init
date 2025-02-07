import threading
import time


# Función que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f"Procesando solicitud {request_id}")
    time.sleep(3)
    print(f"Soliciutd {request_id} completada")


threads = []

for i in range(3):
    # Crear nuevo hilo que ejecutará la función
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    # Asegura que el hilo termine antes de continuar
    thread.join()

print("Todas las solicitudes han sido procesadas")


# ________________________________________________________________________
# |                       |                       |                       |
# |       CONCEPTO        |     CONCURRENCIA      |      PARALELISMO      |
# |_______________________|_______________________|_______________________|
# |                       |  Manejo de múltiples  | Ejecución simultánea  |
# |       Definición      | tareas progresivamente|  de múltiples tareas  |
# |_______________________|_______________________|_______________________|
# |                       |   Operaciones I/O     |  Tareas que requieran |
# |      Usos ideales     |    (Espera de red,    |   mucho cálculo       |
# |                       | Escritura de archivos)|                       |
# |_______________________|_______________________|_______________________|
# |                       |                       |                       |
# |     Implementación    |  threading, asyncio   |    multiprocessing    |
# |_______________________|_______________________|_______________________|
