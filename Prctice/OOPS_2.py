"""
Private Class:
    - This class is intended for internal use within the module.
    - It is not meant to be accessed directly by users of the module.
    - Typically, its name starts with an underscore ( __ ) to indicate its private nature.

Public Class:
    - This class is intended for use by users of the module.
    - It provides the main functionality that the module is designed to offer.
    - It is accessible and documented for external use.
"""

# class Car:
#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("Car is starting")

#     @staticmethod
#     def stop():
#         print("Car is stopping")

# class Toyota(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()
        
# car1 = Toyota("Fortuner","Petrol")
# print(car1.type)
# car2 = Toyota("Innova")

# print(car1.name)
# print(car1.start())
# print(car1.stop())
# print(car1.color)
# print(car2.name)

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Petrol")
# car1.start()
        
# Multiple Inheritance
# class A:
#     varA = "I am A"
# class B:
#     varB = "I am B"
# class C(A,B):
#     varC = "I am C"
# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# Class Method
# class Person:
#     name = "anonymous"

#     # def change_name(self, name):
#     #     self.name = name

#     @classmethod
#     def change_name(cls, name):
#         cls.name = name

# p1 = Person()
# p1.change_name("Bruce")
# print(p1.name)
# print(Person.name)

# Property Decorator
# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#     @property
#     def claculate_percentage(self):
#         return str(round((self.phy + self.chem + self.maths) / 3,2)) + "%"
# stu1 = Student(80,90,95)
# print(stu1.claculate_percentage)
        
# Polymorphism
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
    
#     def display(self):
#         return f"{self.real}i + {self.imag}j"

#     def __add__(self, num2):
#         newreal = self.real + num2.real
#         newimag = self.imag + num2.imag
#         return Complex(newreal, newimag)
# #  We can use all the operators in the same way as we used __add__ method eg: __sub__ , __mul__ , __div__ etc.
# num1 = Complex(2, 3)
# print(num1.display())
# num2 = Complex(5, 1)
# print(num2.display())
# num3 = num1 + num2
# print(num3.display())

# Question define a class Circle with the following methods: Area and Perimeter of the circle.
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
# c1 = Circle(4)
# print("This is the radius of the circle:", c1.area())
# print("This is the perimeter of the circle:", c1.perimeter())

# Question define a class Employee with the following attributes: role, department, salary and a method showDetails. Define another class Engineer which inherits the Employee class and has the following attributes: name, age.
# class Employee:
#     def __init__(self, role , department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
    
#     def showDetails(self):
#         return f"Role: {self.role} \nDepartment: {self.department} \nSalary: {self.salary}"
    
# class Engineer(Employee):
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "Data Analyst", 40000)

    
# emp1 = Employee("Software Developer", "IT", 50000)
# print(emp1.showDetails())
# eng1 = Engineer("Bruce", 25)
# print(eng1.showDetails())

# Question define a class Orders with the following attributes: items, price and a method showDetails. Also, define a method __gt__ in the Orders class to compare the price of two orders.
class Orders:
    def __init__(self, items, price):
        self.items = items
        self.price = price
    def showDetails(self):
        return f"Items: {self.items} \nPrice: {self.price}"
    def __gt__(self, order2):
        return self.price > order2.price
            
order1 = Orders("Pizza", 400)
print(order1.showDetails())
order2 = Orders("Burger", 300)
print(order2.showDetails())
print(order1 > order2)
