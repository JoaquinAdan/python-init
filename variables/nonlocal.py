def outer_function():
    x = "enclosing"

    def inner_function():
        nonlocal x
        x = "modified"
        print("inner:", x)

    inner_function()
    print("outer:", x)


outer_function()
