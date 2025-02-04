x = "global"  # Variable global


# Función externa
def outer_function():
    x = "enclosing"  # Variable no local
    print("outer:", x)

    # Función interna
    def inner_function():
        x = "local"  # Variable local
        print("inner:", x)

    inner_function()


outer_function()
print("global:", x)
