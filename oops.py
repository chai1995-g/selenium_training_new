class Employee:
    def __init__(self, name, age, pay, phone_no):
        self.name = name
        self.age = age
        self.pay = pay
        self.phone_no = phone_no
E1 = Employee("chaithra", 28, 40000, 123456)
E2 = Employee("geetha", 30, 50000, 123456)

print(E2.name)
print(E2.pay)
##############

class Calculator:
   def add(self, a, b):
       return a + b
   def subtract(self, a, b):
       return a - b
   def multiply(self, a, b):
       return a * b
   def divide(self, a, b):
       return a / b
cal = Calculator()
print(cal.add(1, 2))
print(cal.multiply(1, 2))
print(cal.subtract(1, 2))
print(cal.divide(30, 5))
#####
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def age_limit(self):
        if self.age > 18:
            print("the person is above 18 years old")
        else:
            print("the person is below 18 years old")
age_obj = Person("chaithra", 25, "femlae")
age_obj.age_limit()












