import random

def number_guessing_game():
    secret_number = random.randint(1,100)
    guess=None

    print("welcome to the number guessing game!!!")
    print("I'm thinking of a number between 1 & 100 ")
    print("can you guess what it is???")

    while guess !=secret_number:
        guess = int(input("enter your guess"))

        if guess < secret_number:
            print("too low!! try again")
        elif guess > secret_number:
            print("too high!! try again")
        else:
            print("congratulations!!! you guessed the cprrect no")

number_guessing_game()