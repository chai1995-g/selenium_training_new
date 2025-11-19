class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student:
    def __init__(self, stu_id):
        self.stu_id = stu_id
    def details(self):
        print(f"Student ID: {self.stu_id}")

class Teacher(Person, Student):
    def __init__(self, name, age, stu_id, emp_id ):
        Person. __init__(self, name, age)
        Student. __init__(self, stu_id)
        self.emp_id = emp_id
    def details(self):
        print(f"Teacher ID: {self.emp_id}")

class TeachingAssistant(Teacher):
    def __init__(self, name, age, stu_id, emp_id, subject):
        super().__init__(name, age, stu_id, emp_id)
        self.subject = subject

    def details(self):
        super().details()
        print(f"Subject name: {self.subject}")

class1 = TeachingAssistant("John", "19", 123, 789, "english")
class1.details()
class2 = Person("chaitha", 29)
class2.details()
class3 = Student(96)
class3.details()
