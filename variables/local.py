x = 100  # Variable global


def local_function():
    x = 10  # Variable local
    print(f"Variable local: {x}")


def show_global():
    print(f"Variable global: {x}")


local_function()
print(x)
