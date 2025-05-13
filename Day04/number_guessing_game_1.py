import random
number = random.randint(1, 20)
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 20.")
print("You can guess as much as you wish. If you guess the number, you win!")
guess = int(input("Enter your guess: "))
while guess != number:
    if guess > number:
        print("Sorry, you guessed too high. Try again.")
        guess = int(input("Enter your guess: "))
    elif guess < number:
        print("Sorry, you guessed too low. Try again.")
        guess = int(input("Enter your guess: "))

print("Congratulations! You guessed the number!")

print("Thanks for playing!")
print("Goodbye")
