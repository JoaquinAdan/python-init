"""
1. La función recibirá una lista de diccionarios.
Cada diccionario tendrá las claves: "'name', 'age' y 'salary'".

2. La función debe devolver una lista de empleados que ganen más de un cierto sueldo.
"""

employes = [
    {"name": "John", "age": 25, "salary": 50000},
    {"name": "Sarah", "age": 30, "salary": 80000},
    {"name": "Jessica", "age": 35, "salary": 120000},
    {"name": "Mike", "age": 40, "salary": 150000},
    {"name": "Tom", "age": 45, "salary": 200000},
    {"name": "Linda", "age": 50, "salary": 250000},
]


def get_employes(employes, salary):
    """
    Recibe una lista de empleados y un salario.
    Devuelve una lista de empleados que ganen más del salario dado.
    """
    return [employe for employe in employes if employe["salary"] > salary]


get_employes(employes, 100000)
