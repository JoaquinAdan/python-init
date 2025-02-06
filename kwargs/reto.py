# Crear una función que reciba una cantidad variable de productos y sus precios, calcule el total y aplique un descuento opcional si se proporciona como un argumento con nombre
# 1. Usar args para recibir una lista de precios.
# 2. Usar kwargs para aceptar un descuento opcional y aplicarlo al total.


# Formula
# P−(P×(D/100)).  P == Precio , D == Descuento


def total(*args, **kwargs):
    total = sum(args)
    if "discount" in kwargs:
        total -= total * kwargs["discount"] / 100
    return total


print(total(60, 50, discount=20))
