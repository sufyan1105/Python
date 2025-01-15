import os

f = open('practice.txt', 'a')
# data = f.read()
# print(data)

f.write("My name is sufyan ")
f.write("I am a student")
f.close()

os.remove('practice.txt')
