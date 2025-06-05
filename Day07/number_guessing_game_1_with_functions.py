import random

def generate_random_number():
    """Generates a random number between 1 and 20."""
    return random.randint(1, 20)

def welcome_message():
    """Prints a welcome message."""
    print("Welcome to the number guessing game!")
    print("I have selected a number between 1 and 20.")
    print("You can guess as much as you wish. If you guess the number, you win!")

def get_user_guess():
    """Asks the user to enter a guess and returns it as an integer."""
    return int(input("Enter your guess: "))

def give_feedback(guess, number):
    """Prints feedback based on the user's guess."""
    if guess > number:
        print("Sorry, you guessed too high. Try again.")
    elif guess < number:
        print("Sorry, you guessed too low. Try again.")

def end_message():
    """Prints the ending message."""
    print("Congratulations! You guessed the number!")
    print("Thanks for playing!")
    print("Goodbye")

def play_game():
    """Main function to play the guessing game."""
    number = generate_random_number()
    welcome_message()

    guess = get_user_guess()
    while guess != number:
        give_feedback(guess, number)
        guess = get_user_guess()

    end_message()

play_game()
