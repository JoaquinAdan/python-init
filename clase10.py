numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers[2])
information = {"nombre": "Joaco", "apellido": "Perez", "edad": 20, "altura": 1.50}
print(information)
del information["edad"]
print(information)
claves = information.keys()
print(claves)
values = information.values()
print(values)
items = information.items()
print(items)
contacts = {
    "Joaco": {"nombre": "Joaco", "apellido": "Perez", "edad": 20, "altura": 1.50},
    "Ana": {"nombre": "Ana", "apellido": "Gomez", "edad": 25, "altura": 1.60},
}

print(contacts["Joaco"])
# Configuración de una aplicación
config = {"host": "localhost", "port": 8080, "debug": True}
print("Configuración:", config)

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25},
}
print("Datos de usuario user123:", usuarios["user123"])

# Almacenamiento de datos estructurados
libro = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967,
}
print("Datos del libro:", libro)

# Datos en formato JSON
import json

json_data = json.dumps(libro)
print("Datos en JSON:", json_data)
