# 1. Un método estático para verificar si el monto de un pedido es mayor a un minimo permitido (por ejemplo, $50).
# 2. Un método de clase que permita crear un pedido aplicando un descuento global


class Order:
    global_discount = 20
    min_price = 50

    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount

    @staticmethod
    def calculate_min(amount: int) -> int:
        if amount < Order.min_price:
            return False
        return True

    # P−(P×(D/100)).  P == Precio , D == Descuento

    @classmethod
    def create_order(cls, amount):
        print(amount)
        price_with_discount = amount - (amount * cls.global_discount / 100)
        print(price_with_discount)
        return amount - (amount * cls.global_discount / 100)


print(Order.calculate_min(50))


# print(Order.global_discount)
# Order.update_global_discount(15)
# print(Order.global_discount)

create_order = Order.create_order(100)
print(create_order)
