# Implementar una clase CuentaBancaria con un método protegido para actualizar el saldo y un metodo privado para registar las trasnsacciones internamente
# 1. El método protegido (_actualizar_saldo)solo debe ser utilizado dentro de la clase y sus subclases
# 2. El método privado (__registrar_transaccion) debe ser completamente interno y no accesible fuera de la clase


class CuentaBancaria:
    def __init__(self, dinero: int):
        self.dinero = dinero
        self.transacciones = [dinero]

    def _actualizar_saldo(self, dinero: int) -> None:
        self.dinero += dinero

    def __registrar_transaccion(self, dinero: int) -> None:
        self.transacciones.append(dinero)

    def recibir_dinero(self, dinero: int) -> None:
        self._actualizar_saldo(dinero)
        self.__registrar_transaccion(dinero)

    def get_dinero(self) -> int:
        print(self.dinero)
        return self.dinero

    def get_transacciones(self) -> list[int]:
        print(self.transacciones)
        return self.transacciones


cuenta1 = CuentaBancaria(100)

cuenta1.get_dinero()
cuenta1.get_transacciones()

cuenta1.recibir_dinero(20)
cuenta1.recibir_dinero(30)

cuenta1.get_dinero()
cuenta1.get_transacciones()
