# def sum(a,b):
#     return a+b
# print(sum(5,7))

# def average(a,b,c):
#     return (a+b+c)/3
# print(average(1,2,3))

# Q1: Write a function that takes a string as an argument and returns the length of the string
# def length(a):
#     return len(a)
# sen = "Hello, my name is John"
# print(length(sen))

# Q2: Write a function that takes a list as an argument and returns the sum of the list on the same line
# def print_list(list):
#     for i in list:
#         print(i, end=" ")
# list = [1,2,3,4,5]
# print_list(list)

# Q3: To find the factiorial of number n
# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(fact(5))

# Q4: USD to INR conversion
# def conversion(a):
#     inr = a*83
#     return (f"The amount in INR is {inr}")
# print(conversion(73))

# Q5: A function that returns if the number is even or odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(4))
print(even_odd(5))
