import random

def generate_number():
    return random.randint(1, 20)

def get_guess():
    return input("Enter your guess: ")

def check_guess(guess, number):
    if guess > number:
        print("Sorry, you guessed too high. Try again.")
        return False
    elif guess < number:
        print("Sorry, you guessed too low. Try again.")
        return False
    else:
        print("Congratulations! You guessed the number!")
        return True

def is_exit_command(guess):
    return guess.lower() == 'x'