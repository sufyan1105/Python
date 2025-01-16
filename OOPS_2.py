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

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")

class Toyota(Car):
    def __init__(self,name):
        self.name = name
        
car1 = Toyota("Fortuner")
car2 = Toyota("Innova")

print(car1.name)
print(car1.start())
print(car1.stop())
print(car1.color)
print(car2.name)
