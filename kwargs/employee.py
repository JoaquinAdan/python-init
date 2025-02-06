class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print(f"Name: {self.name}")
        print("Skills:", self.skills)
        print("Details:", self.details)


employee = Employee(
    "John", "Python", "Java", "C++", age=25, city="New York", job="Developer"
)
employee.show_employee()
