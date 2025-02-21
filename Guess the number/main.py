import random 

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    

def check_answer(guess, answer, turns):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
    elif guess > answer:
        print("Too high.")
        return turns - 1
    else:
        print("Too low.")
        return turns - 1        

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
answer = random.randint(1, 100)
turns = set_difficulty()

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guess = int(input("Make a guess: "))
print(f"You have {turns} attempts remaining to guess the number.")