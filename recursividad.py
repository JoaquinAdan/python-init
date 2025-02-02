# Factorial de un número
# 5! = 5 * 4 * 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1

# 5! = 5 * 4!
# 4! = 4 * 3!

# facotorial(N) = N * factorial(N-1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial_5 = factorial(10)

# print(factorial_5)

# Fibonacci

# 0 1 1 2 3 5 8 13 21 34 ...

#             / caso base
#             | f(0) = 0
# Fibonacci  <  f(1) = 1
#             | caso recursivo
#             \ f(N-1)+F(N-2)
#

# def fibonacci(n, a=0, b=1, numbers=None):
#     if numbers is None:
#         numbers = []

#     if a < n:
#         numbers.append(a)
#         return fibonacci(n, b, a + b, numbers)

#     return numbers


# print(fibonacci(14))

# para obtener que numero esta en cada posicion sin contar el 0
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 6
# print(fibonacci(number))

# def factorial_add(n):
#     if n == 0:
#         return 1
#     else:
#         return n + factorial_add(n - 1)


# factorial_add_5 = factorial_add(5)

# print(factorial_add_5)

def factorial_add(n):
    if n <= 0:
        return 0
    else:
        return n + factorial_add(n - 1)


factorial_add_5 = factorial_add(10)

print(factorial_add_5)
