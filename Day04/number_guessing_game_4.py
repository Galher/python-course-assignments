import random

number = random.randint(1, 20)
show_number = False 

print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 20.")
print("You can guess as much as you wish. If you guess the number, you win!")
print("Type 'd' to toggle debug mode (show/hide the number).")
print("Type 'x' to exit the game.")

guess = input("Enter your guess: ")

while guess != 'x':
    if guess  == 'd':
        show_number = not show_number
        if show_number:
            print("Debug mode ON. The number is:", number)
        else:
            print("Debug mode OFF.")
        guess = input("Enter your guess: ")
        continue
    if guess == 's':
        print("The number is", number)
        guess = input("Enter your guess: ")
        continue
    elif guess.isdigit():
        guess = int(guess)

        if guess > number:
            print("Sorry, you guessed too high. Try again.")
        elif guess < number:
            print("Sorry, you guessed too low. Try again.")
        else:
            print("Congratulations! You guessed the number!")
            print("Thanks for playing!")
            print("Goodbye")
            break

        if show_number:
            print("[DEBUG] The number is:", number)

   
    else:
        print("Invalid input. Please enter a number between 1 and 20, 'd' to toggle debug, or 'x' to exit.")

    guess = input("Enter your guess: ") 

print("You have exited the game.")
print("Goodbye")

