# 1. Funciones para **agregar** y **eliminar** empleados de una lista.

# 2. Un bloque `if __name__ == "__main__":` que permita probar el funcionamiento del script ejecutándo directamente.

employees = ["Juan", "María", "Pedro", "Luis", "Ana"]


def add_employee(employee):
    employees.append(employee)
    return employees


def remove_employee(employee):
    employees.remove(employee)
    return employees


if __name__ == "__main__":
    print("Lista de empleados")
    print(employees)
    print("Agregando un empleado")
    print(add_employee("Carlos"))
    print("Eliminando un empleado")
    print(remove_employee("María"))
    print(remove_employee("Juan"))
    print(remove_employee("Luis"))
