class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! My name is " + self.name)


class Student(Person):
    def __init__(self, name, age, grade) -> None:
        Person.__init__(self, name, age)
        self.grade = grade

    def sleeping(self, hours) -> str:
        print(f"{self.name} has slept for {hours} hours")


a = Student(name="John", age=15, grade=10)
a.greet()
a.sleeping(10)
