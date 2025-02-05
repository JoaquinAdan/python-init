def save_actions(func):
    def wrapper(self):
        action = func(self) + "\n"
        with open("./decoradores/acciones.txt", "a") as file:
            file.write(action)
        return action

    return wrapper


class Employee:
    def __init__(self, name):
        self.name = name

    @save_actions
    def greet(self):
        return f"¡Hola! Soy {self.name}"

    @save_actions
    def work(self):
        return "Trabajando"

    @save_actions
    def cook(self):
        return "Cocinando"


empleado1 = Employee("Juan")

empleado1.cook()
empleado1.work()
empleado1.greet()
empleado1.cook()
