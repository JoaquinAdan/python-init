from collections import defaultdict
from enum import Enum


class OrderStatus(Enum):
    PENDING = 1  # Pendiente
    SHIPPED = 2  # Enviado
    DELIVERED = 3  # Entregado


class ProductManagement:
    def __init__(self):
        # Usamos defaultdict(int) para almacenar los productos con sus cantidades
        self.products = defaultdict(int)
        self.orders = defaultdict(int)
        self.selled_products = defaultdict(int)

    def add_products(self, new_products: list[str]) -> None:
        """
        Agrega productos al inventario y actualiza el conteo.
        """
        for product in new_products:
            self.products[product] += 1  # Incrementa el conteo del producto

    def get_products(self) -> dict[str, int]:
        """
        Retorna los productos como un diccionario con su conteo.
        """
        return dict(
            self.products
        )  # Convertimos defaultdict a dict para evitar comportamiento inesperado

    def add_orders(self, orders: list[str]) -> None:
        """
        Agrega pedidos a la lista de órdenes dependiendo de que haya stock, y actualiza el conteo.
        """
        for order in orders:
            if self.products[order] > 0:
                self.orders[order] += 1  # Incrementa el conteo del pedido
                self.products[order] -= 1  # Decrementa el conteo del producto
                self.selled_products[order] += 1
            else:
                print(f"No hay stock para el pedido {order}")

    def get_orders(self) -> dict[str, int]:
        """
        Retorna los pedidos como un diccionario con su conteo.
        """
        return dict(self.orders)

    def get_selled_products(self) -> dict[str, int]:
        """
        Retorna los productos vendidos como un diccionario con su conteo.
        """
        return dict(self.selled_products)


# Pruebas
management = ProductManagement()

products = ["laptop", "smarthphone", "tablet"]
products2 = ["laptop", "smarthphone", "tablet", "laptop", "playstation"]

management.add_products(products)
management.add_products(products2)

print("Productos:", management.get_products())

orders = ["laptop", "smarthphone", "tablet", "laptop", "playstation"]
management.add_orders(orders)
print("Ordenes:", management.get_orders())

print("Productos:", management.get_products())

management.add_orders(orders)
print("Ordenes:", management.get_orders())

print("Productos vendidos:", management.get_selled_products())
