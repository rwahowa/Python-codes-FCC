import random

def guess_number(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = input(f"Guess a number between 1 and {x} : ")
        print(guess)

guess_number(10)

