import random
number = random.randint(1, 20)
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 20.")
print("You can guess as much as you wish. If you guess the number, you win!")
print("If you want to exit the game, type 'x'")
guess = input("Enter your guess: ")
# create a while loop that will run until the user guesses the number or types 'x' to exit
while guess != 'X':
    if guess.isdigit():
        guess = int(guess)
        if guess > number:
            print("Sorry, you guessed too high. Try again.")
            guess = input("Enter your guess: ")
        elif guess < number:
            print("Sorry, you guessed too low. Try again.")
            guess = input("Enter your guess: ")
        else:
            print("Congratulations! You guessed the number!")
            print("Thanks for playing!")
            print("Goodbye")
            break
    elif guess != 'x':
        print("Invalid input. Please enter a number between 1 and 20 or 'x' to exit.")
        guess = input("Enter your guess: ")
    if guess == 'x':
        print("You have exited the game.")
        break



