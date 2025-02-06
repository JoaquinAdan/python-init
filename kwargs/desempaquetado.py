# Desempaquetado de args
def add(a, b, c):
    return a + b + c


values = (1, 2, 3)
print(add(*values))


# Desempaquetado de kwargs
def show_info(name, age):
    print(f"Name: {name}, Age: {age}")


data = {"name": "John", "age": 30}
show_info(**data)
