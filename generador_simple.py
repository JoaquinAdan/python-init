def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)


def contador():
    num = 1
    while True:
        yield num
        num += 1


gen = contador()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))
