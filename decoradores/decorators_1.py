def log_decorator(func):
    def wrapper():
        print("1 Log de la transaccipon...")
        func()
        print("3 Log terminado...")

    return wrapper


@log_decorator
def process_payment():
    print("2 Procesando pago...")


process_payment()
