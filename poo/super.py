class LivingBeing:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"LivingBeing({self.name})"


class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(
            f"Hi, I'm {self.name} and I'm {self.age} years old, and my student ID is {self.student_id}"
        )


student1 = Student("Jose", 20, 123)

student1.introduce()
