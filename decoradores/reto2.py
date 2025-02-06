# Implementa una clase Producto
# 1. Utiliza @property para controlar el acceso y modificación del precio.
# 2. Implementa validación para asegurarse de que el precio y el stock no puedan ser negativos.
# 3. Define un método que calcule el valor total del inventario
# 4. deleeter para borrar todo el inventario


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = precio
        self._stock = stock

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, new_precio):
        if new_precio < 0:
            raise ValueError("Precio no puede ser negativo")
        self._precio = new_precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock no puede ser negativo")
        self._stock = new_stock

    def valor_inventario(self):
        return self.precio * self.stock

    @precio.deleter
    def precio(self):
        print(f"El precio del producto {self.nombre} ha sido eliminado")
        del self._precio
        del self._stock
