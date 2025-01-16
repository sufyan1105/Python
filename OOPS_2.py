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
class Person:
    name = "anonymous"

    # def change_name(self, name):
    #     self.name = name
    
    @classmethod
    def change_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("Bruce")
print(p1.name)
print(Person.name)
