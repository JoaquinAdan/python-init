def divide(a: int, b: int) -> float:
    # Validar que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parametros deben ser enteros")
    # Verificamos que el divisor no sea cero
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b


# Ejemplo de uso

# try:
#     res = divide(10, "2")  # Error de tipo
#     print(res)
# except TypeError as e:
#     print(f"Error: {e}")

# try:
#     res = divide(10, 0)  # Error de división entre cero
#     print(res)
# except ValueError as e:
#     print(f"Error: {e}")

try:
    res = divide(10, 2)
    print(res)
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
