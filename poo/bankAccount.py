class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(
                f"Se ha depositado {amount} en la cuenta de {self.account_holder}, saldo actual: {self.balance}"
            )
        else:
            print("Cuenta inactiva, no se puede depositar")

    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(
                    f"Se ha retirado {amount} de la cuenta de {self.account_holder}, saldo actual: {self.balance}"
                )
            else:
                print("Saldo insuficiente")
        else:
            print("Cuenta inactiva, no se puede retirar")

    def deactivate(self):
        self.is_active = False
        print(f"Cuenta de {self.account_holder} desactivada, has perdido {self.balance}")
        
    def activate(self):
        self.is_active = True
        print(f"Cuenta de {self.account_holder} activada, pero perdiste {self.balance}, arrancas de 0")
        self.balance = 0
        
    def check_balance(self):
        if self.is_active:
            print(f"El saldo de la cuenta de {self.account_holder} es: {self.balance}")
        return self.balance
        
        
cuenta1 = BankAccount("Juan", 1000)
cuenta1.deposit(500)
cuenta1.check_balance()
cuenta1.withdraw(200)
cuenta1.deactivate()
cuenta1.deposit(500)
cuenta1.activate()
cuenta1.check_balance()