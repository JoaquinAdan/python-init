# Implementa una función que procese una lista de diccionarios con información de empleados, utilizando anotaciones de tipo.
# 1. Recibirá una lista de diccionarios. Cada diccionario tendrá las claves: "nombre", "edad" y "sueldo"
# 2. Debe devolver una lista de empleados que ganen más de cierto sueldo

employees = [
    {"nombre": "Juan", "edad": 25, "sueldo": 1000},
    {"nombre": "Ana", "edad": 30, "sueldo": 1500},
    {"nombre": "Pedro", "edad": 35, "sueldo": 2000},
    {"nombre": "María", "edad": 40, "sueldo": 2500},
    {"nombre": "Luis", "edad": 45, "sueldo": 3000},
]


def process_employees(employees: dict[str, int], salary: int) -> list[str]:
    return [employee["nombre"] for employee in employees if employee["sueldo"] > salary]


print(process_employees(employees, 1000))
