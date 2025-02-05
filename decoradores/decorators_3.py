# Decorador que comprueba si un empleado tiene un rol especifico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            # Si el rol del empleado coincide con el rol requerido
            if employee["role"] == required_role:
                return func(employee)
            else:
                print(f"Acceso denegado. Solo {required_role} puede eliminar empleados")

        return wrapper

    return decorator


def log_action(func):
    def wrapper(employee):
        print(f"Registrando la acción de {func.__name__} en el sistema")
        return func(employee)

    return wrapper


@check_access("admin")
@log_action
def delete_employee(employee):
    print(f"El empleado {employee["name"]}, ha sido eliminado")


admin = {"name": "Juan", "role": "admin"}
employee = {"name": "Pedro", "role": "user"}

delete_employee(admin)
delete_employee(employee)
