#  Class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).    

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Constructor Called")

# s1 = Student("Sufyan", 21)
# print(s1.name, s1.age)

# print(s1.name)

# class Car:
#     color = "Blue"
# c1 = Car()
# print(c1.color)  # Output: Blue

# Q1
class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    @staticmethod 
    def hello():
        print("Hello")

    def FindAverage(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hello", self.name,"your average marks are", round(sum/len(self.marks),2))
        

s1 = Student("Sufyan", [90,92,96])
s1.FindAverage()
s1.hello()
        
