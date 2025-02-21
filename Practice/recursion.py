# Recursive function 
# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)
# show(5)

# Recursion returns n! (n factorial)
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

# Recursive function to calculate the sum of n natural numbers
# def sum(n):
#     if n == 1:
#         return 0
#     else:
#         return n + sum(n-1)
# print(sum(5))

# Recursive funtion to print all the elements of a list
def print_list(list, idx=0):
    if idx == len(list):
        return 
    print(list[idx])
    print_list(list, idx+1)

# list = [1, 2, 3, 4, 5]
list = ['a', 'b', 'c', 'd', 'e']
print_list(list)