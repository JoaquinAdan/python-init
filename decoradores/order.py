class Order:

    @staticmethod
    def calculate_tax(amount: int, tax_rate: int) -> int:
        return amount * (tax_rate / 100)


print(Order.calculate_tax(1000, 18))
