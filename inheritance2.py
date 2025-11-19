class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def method(self):
        print(f"name: {self.name}, age: {self.age}")
class Fulltime:
    def __init__(self, salary):
        self.salary = salary
    def method1(self):
        print(f"salary: {self.salary}")

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id
    def employee1(self):
        print(f"employee id: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age, emp_id)
        self.department = department
    def manager1(self):
        print(f"department name: {self.department}")

class Hr(Person, Fulltime):
    def __init__(self, name, age, salary, hr_policy):
        Person.__init__(self, name, age)
        Fulltime.__init__(self, salary)
        self.hr_policy = hr_policy
    def hr_policy1(self):
        print(f"name: {self.name}, hr_policy: {self.hr_policy}")

class Intern(Person):
    def __init__(self, name, age, stipend):
        super().__init__(name, age)
        self.stipend = stipend
    def Intern1(self):
        print(f"stipend: {self.stipend}")


class2 = Person("chaithra", 40)
class2.method()








