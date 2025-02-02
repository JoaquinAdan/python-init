# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b


# def even(limit):
#     a = 1
#     while a < limit + 1:
#         if a % 2 == 0:
#             yield a
# a += 1


def odd(limit):
    a = 1
    while a < limit + 1:
        yield a
        a += 2


for num in odd(20):
    print(num)


def even(limit):
    a = 0
    while a < limit + 1:
        # if a % 2 != 0:
        yield a
        a += 2


# for num in even(20):
#     print(num)

gen = even(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
