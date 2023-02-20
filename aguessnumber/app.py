# Guess a number game. It has to be the number, the computer is holding in memory
import random

def guess_number(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))

        if guess < random_number:
            print(f"Your guess ({guess}) is lower. Try again")
        elif guess > random_number:
            print(f"Your guess ({guess}) is higher. Try again")

    print(f"Your guess of {random_number} is correct")       
guess_number(random.randint(10,35))

