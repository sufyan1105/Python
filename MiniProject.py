# Guess the number game
import random 

target = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100. Can you guess it?")
guess = int(input("Enter your guess: "))
while guess != target:
    if guess < target:
        print("Higher!")
    else:
        print("Lower!")
    guess = int(input("Enter your guess: "))
print("Congratulations! You guessed the number correctly!")
print("The number was", target)
print("Thanks for playing!")




