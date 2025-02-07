# Una corrutina es una funcion que puede pausarse y reanudarse. Se define con la palabra clave async await.
import asyncio


async def process_data(data):
    print(f"Procesando {data}...")
    # Simular una operación
    await asyncio.sleep(3)
    print(f"{data} procesado.")
    return data * 2


async def main():
    print("Iniciando proceso")
    result = await process_data("archivo.txt")
    print(f"Resultado: {result}")


asyncio.run(main())
