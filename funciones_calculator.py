def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def not_a_number(num):
    while not num.isnumeric():
        print("Invalid number")
        num = input("Ingrese el primer numero: ")


def calculator():
    print("Calculator")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    option = input("Select an option: ")
    if option == "5":
        print("Bye")
        return
    if option in ["1", "2", "3", "4"]:
        num1_input = input("Ingrese el primer numero: ")
        not_a_number(num1_input)
        num2_input = input("Ingrese el segundo numero: ")
        not_a_number(num2_input)

        num1 = float(num1_input)
        num2 = float(num2_input)
        
        if option == "1":
            print(f"Resultado: {add(num1, num2)}")
        elif option == "2":
            print(f"Resultado: {substract(num1, num2)}")
        elif option == "3":
            print(f"Resultado: {multiply(num1, num2)}")
        elif option == "4":
            print(f"Resultado: {divide(num1, num2)}")
        else:
            print("Invalid option")
            calculator()
    else:
        print("Invalid option")
        calculator()


calculator()
