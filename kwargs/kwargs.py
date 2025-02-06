def print_info(**kwargs):
    print(kwargs)
    print(kwargs.items())
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=25, city="New York")
print_info(name="Jane", age=30, city="Los Angeles", job="Developer")
