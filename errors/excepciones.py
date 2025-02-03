try:
    divisor = int(input("Introduce un número divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print("Ha ocurrido un error:", e)
except ValueError as e:
    print("Error: Debes introducir un número")
    print("Ha ocurrido un error:", e)
# except ArithmeticError as e:
#     print("Error aritmético")
#     print("Ha ocurrido un error:", e)
