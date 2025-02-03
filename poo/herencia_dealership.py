class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulamiento
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El auto {self.model} ha sido vendido")
        else:
            print(f"El auto {self.model} no está disponible")

    # Abstracción
    def check_available(self):
        return self.is_available

    # Abstracción
    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")


# Herencia
class Car(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if self.is_avaliable:
            return print(f"El motor del auto {self.brand} se ha encendido")
        else:
            return print(f"El auto {self.brand} no está disponible")

    # Polimorfismo
    def stop_engine(self):
        if self.is_avaliable:
            return print(f"El motor del auto {self.brand} se ha apagado")
        else:
            return print(f"El auto {self.brand} no está disponible")


# Herencia
class Bike(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if self.is_avaliable:
            return print(f"La bicileta {self.brand} Esta en marcha")
        else:
            return print(f"La bicicleta {self.brand} no está disponible")

    # Polimorfismo
    def stop_engine(self):
        if self.is_avaliable:
            return print(f"La bicileta {self.brand} se ha detenido")
        else:
            return print(f"La bicicleta {self.brand} no está disponible")


# Herencia
class Truck(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if self.is_avaliable:
            return print(f"El motor del camion {self.brand} se ha encendido")
        else:
            return print(f"El camion {self.brand} no está disponible")

    # Polimorfismo
    def stop_engine(self):
        if self.is_avaliable:
            return print(f"El motor del camion {self.brand} se ha apagado")
        else:
            return print(f"El camion {self.brand} no está disponible")


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            self.purchased_vehicles.append(vehicle)
            vehicle.sell()
        else:
            print(f"El vehículo {vehicle.model} no está disponible")

    def inquire_vehicles(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(
            f"El vehículo {vehicle.brand} está {availability} y cuesta {vehicle.get_price()}"
        )


class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"Se ha agregado el vehículo {vehicle.brand} al inventario")

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"Se ha agregado al cliente {customer.name}")

    def show_available_vehicles(self):
        print("Vehículos disponibles:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- el {vehicle.brand} por {vehicle.get_price()}")


car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Ford", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)
dealership.register_customer(customer1)

# Mostrar vehiculos disponibles
dealership.show_available_vehicles()

# Consultar vehiculos
customer1.inquire_vehicles(car1)

# Cliente compra en vehiculo
customer1.buy_vehicle(car1)

# Mostrar vehiculos disponibles
dealership.show_available_vehicles()


# ¿Qué es la abstracción en programación orientada a objetos?
# La abstracción te permite definir estructuras básicas sin entrar en detalles específicos. En el código, hemos creado instancias de diferentes vehículos, como un auto, una bicicleta y un camión, asignándoles atributos como marca, modelo y precio. Este enfoque nos permite trabajar con conceptos generales antes de precisar características específicas.

# ¿Cómo se aplica el encapsulamiento?
# El encapsulamiento se refiere a mantener los datos privados dentro de una clase y acceder a ellos solo mediante métodos públicos. En nuestro ejemplo, las variables de instancia de los vehículos son privadas. Solo podemos acceder a ellas a través de métodos específicos, como GetPrice o verificarDisponibilidad, asegurando así que los datos se manejen de manera controlada y segura.

# ¿Qué rol juega la herencia?
# La herencia permite que una clase hija adopte atributos y métodos de una clase padre. Aquí, la clase auto hereda de la clase vehículo, lo que significa que todas las características y comportamientos definidos en vehículo están disponibles en auto sin necesidad de duplicar el código. Este principio facilita la reutilización y extensión del código.

# ¿Qué es el polimorfismo y cómo se usa?
# El polimorfismo permite que diferentes clases respondan a los mismos métodos de maneras distintas. En nuestro caso, tanto el auto como la bicicleta heredan métodos de vehículo, pero cada uno los implementa de forma diferente. Por ejemplo, el método para indicar que el auto está en marcha difiere del método de la bicicleta, que no usa motor. Este comportamiento flexible es clave para escribir código más dinámico y reutilizable.
