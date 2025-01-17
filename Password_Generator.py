# Random password generator
import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation

print(random.choice(charValues))
password = ""
n = int(input("Enter the length of the password: "))
for i in range(n):
    password += random.choice(charValues)
print(password)
