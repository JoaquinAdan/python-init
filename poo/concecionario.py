# Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.


class Vehicle:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.available = True

    def show_vehicle(self):
        print(
            f"Auto modelo {self.model}, precio: {self.price}, disponibilidad: {"si" if self.available else "no"}"
        )

    def sell_vehicle(self):
        if self.available:
            self.available = False
            print(f"El vehiculo {self.model} ha sido vendido")
        else:
            print(f"El vehiculo {self.model} no está disponible")


class User:
    def __init__(self, name, money, user_id):
        self.name = name
        self.money = money
        self.user_id = user_id
        self.vehicles = []

    def buy_vehicle(self, vehicle):
        if vehicle.available and self.money >= vehicle.price:
            vehicle.sell_vehicle()
            self.money -= vehicle.price
            self.vehicles.append(vehicle)
        else:
            print(f"El vehiculo {vehicle.model} no está disponible")

    def show_vehicles(self):
        # for vehicle in self.vehicles:
        print(f"Vehiculos de {self.name}: {', '.join(vehicle.model for vehicle in self.vehicles)}")


class Concessionaire:
    def __init__(self):
        self.vehicles = []
        self.users = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(
            f"El vehiculo {vehicle.model}, con precio ${vehicle.price} ha sido agregado"
        )

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_vehicles(self):
        for vehicle in self.vehicles:
            print(
                f"{vehicle.model} - ${vehicle.price} - {'Disponible' if vehicle.available else 'No disponible'}"
            )

    def show_users(self):
        for user in self.users:
            print(f"{user.name} - {user.user_id}")


car1 = Vehicle("Ferrari", 1000000)
car2 = Vehicle("Lamborghini", 2000000)
car3 = Vehicle("Bugatti", 3000000)

user1 = User("Juan", 10000000, 1)

concessionaire = Concessionaire()

concessionaire.add_vehicle(car1)
concessionaire.add_vehicle(car2)
concessionaire.add_vehicle(car3)

concessionaire.register_user(user1)

concessionaire.show_vehicles()

user1.buy_vehicle(car1)

concessionaire.show_vehicles()

user1.show_vehicles()

user1.buy_vehicle(car3)

user1.show_vehicles()
