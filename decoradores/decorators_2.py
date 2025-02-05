def check_access(func):
    def wrapper(employee):
        # Comprobar el role "admin" para poder eliminar
        if employee.get("role") == "admin":
            return func(employee)
        else:
            print("ACCESO DENEGADO. No tienes permisos para eliminar empleados.")

    return wrapper


@check_access
def delete_employee(employee):
    print(f"Empleado {employee['name']} ha sido eliminado")


admin = {"name": "Juan", "role": "admin"}
employee = {"name": "Pedro", "role": "user"}

delete_employee(admin)
delete_employee(employee)
