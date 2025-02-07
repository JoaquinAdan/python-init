# Implementar un sistema de descarga de archivos asincrónica, donde cada archivo tarde un tiempo variable en descargarse.
import asyncio
import random


tiempo_de_descarga = random.randint(1, 5)


async def process_data():
    print(f"Descargando archivo...")
    print(tiempo_de_descarga)
    await asyncio.sleep(tiempo_de_descarga)
    print(f"Archivo descargado.")


asyncio.run(process_data())
