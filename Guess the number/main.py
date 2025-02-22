import random 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

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
def game():

    answer = random.randint(1, 100)
    turns = set_difficulty()

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_answer(guess, answer, turns)
        if turns <= 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
            turns = turns - 1
        
game()




