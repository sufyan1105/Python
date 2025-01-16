#  Class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).    

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor Called")

s1 = Student("Sufyan", 21)
print(s1.name, s1.age)

# print(s1.name)

# class Car:
#     color = "Blue"
# c1 = Car()
# print(c1.color)  # Output: Blue


