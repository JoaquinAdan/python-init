class BaseClass:
    def __init__(self):
        self._protected_variable = "Protected"
        self.__private_variable = "Private"

    def _protected_method(self):
        print("Este es un metodo protegido")

    def __private_method(self):
        print("Este es un metodo privado")

    def public_method(self):
        self.__private_method()
        print(self.__private_variable)


base = BaseClass()

# print(base._protected_variable)
# base._protected_method()

# base.__private_method()
# print(base.__private_variable)

base.public_method()
