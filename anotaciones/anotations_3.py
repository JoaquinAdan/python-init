class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Mi nombre es {self.name}, tengo {self.age} años"


employee1 = Employee("Juan", 30, 1000.0)
print(employee1.introduce())
