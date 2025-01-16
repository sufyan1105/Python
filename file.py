import os

# f = open('practice.txt', 'a')
# # data = f.read()
# # print(data)

# f.write("My name is sufyan ")
# f.write("I am a student")
# f.close()

# os.remove('practice.txt')

# with open("practice.txt", "w") as f:
#     f.write("My name is sufyan ")
#     f.write("I am a student")
    
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)
# newData = data.replace("sufyan", "Joy")
# print(newData)
# with open("practice.txt", "w") as f:
#     f.write(newData)

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if "name" in data:
#         print("Yes")
#     else:
#         print("No")

count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)


