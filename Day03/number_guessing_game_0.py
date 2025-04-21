#the user needs to guess a number between 1 and 20
#the user has 1 attempts to guess the number
#the user will be told if they are correct or not
#the user will be told if they are too high or too low 
import random
number = random.randint(1, 20)
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 20.")
print("You have 1 attempt to guess the number.")
print("If you guess the number, you win!")
print("If you guess too high, I will tell you you are too high.")
print("If you guess too low, I will tell you you are too low.")
print("Good luck!")
guess = int(input("Enter your guess: "))
if guess == number:
    print("Congratulations! You guessed the number!")
elif guess < number:
    print("Sorry, you guessed too low. The number was", number)
else:
    print("Sorry, you guessed too high. The number was", number)
print("Thanks for playing!")
print("Goodbye!")
