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
# class Student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod 
#     def hello():
#         print("Hello")

#     def FindAverage(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hello", self.name,"your average marks are", round(sum/len(self.marks),2))
        

# s1 = Student("Sufyan", [90,92,96])
# s1.FindAverage()
# s1.hello()
        
# class car():
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.brk = True
#         self.clutch = True
#         self.acc = True

#         print("Car Started")

# car1 = car()
# car1.start()

class acount():
    def __init__(self,balance,accno):
        self.balance = balance
        self.accno = accno

    # Debit
    def debit(self, amount):
        self.balance -= amount
        print("Debited amount is", amount)
        # print("Remaining balance is", self.balance)
    # Credit
    def credit(self, amount):
        self.balance += amount
        print("Credited amount is", amount)
        # print("Remaining balance is", self.balance)
    # Check Balance
    def check_balance(self):
        print("Your balance is", self.balance)

acc1 = acount(1000, 123456)
# print(acc1.balance)
# print(acc1.accno)
acc1.debit(500)
acc1.credit(1000)
acc1.check_balance()