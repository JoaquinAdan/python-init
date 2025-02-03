# Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def show_car(self):
        print(
            f"Auto modelo {self.model}, precio: {self.price}, disponibilidad: {"si" if self.available else "no"}"
        )

    def sell_car(self):
        if self.available:
            self.available = False
            print(f"El auto {self.model} ha sido vendido")
        else:
            print(f"El auto {self.model} no está disponible")

    def check_availability(self):
        return self.available

    def get_price(self):
        return self.price


class User:
    def __init__(self, name, money, user_id):
        self.name = name
        self.money = money
        self.user_id = user_id
        self.cars = []

    def buy_car(self, car):
        if car.available and self.money >= car.price:
            car.sell_car()
            self.money -= car.price
            self.cars.append(car)
        else:
            print(
                f"El auto {car.model} no está disponible o no tienes suficiente dinero"
            )

    def show_cars(self):
        # for car in self.cars:
        print(
            f"autos de {self.name}: {', '.join(car.model for car in self.cars)}"
        )

    def inquire_car(self, car):
        print(
            f"El auto {car.model} cuesta {car.price} y {'esta disponible' if car.available else 'no esta disponible'}"
        )


class Concessionaire:
    def __init__(self):
        self.cars = []
        self.users = []

    def add_car(self, car):
        self.cars.append(car)
        print(
            f"El auto {car.model}, con precio ${car.price} ha sido agregado"
        )

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_cars(self):
        for car in self.cars:
            print(
                f"{car.model} - ${car.price} - {'Disponible' if car.available else 'No disponible'}"
            )

    def show_users(self):
        for user in self.users:
            print(f"{user.name} - {user.user_id}")


car1 = Car("Toyota", "Corolla", 100000)
car2 = Car("Ford", "Fiesta", 50000)
car3 = Car("Chevrolet", "Onix", 80000)

user1 = User("Juan", 10000000, 1)

concessionaire = Concessionaire()

concessionaire.add_car(car1)
concessionaire.add_car(car2)
concessionaire.add_car(car3)

concessionaire.register_user(user1)

concessionaire.show_cars()

user1.inquire_car(car1)

user1.buy_car(car1)

user1.show_cars()

user1.buy_car(car3)

user1.inquire_car(car1)

user1.show_cars()
