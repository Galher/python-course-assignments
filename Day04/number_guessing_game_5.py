import random

number = random.randint(1, 20)
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 20.")
print("You can guess as much as you wish. If you guess the number, you win!")
print("Type 'x' to exit, 'd' to toggle debug mode, and 'm' to toggle move mode.")

show_number = False
move_mode = False

guess = input("Enter your guess: ")

while guess != 'x':
    if guess == 'd':
        show_number = not show_number
        print(f"Debug mode {'ON' if show_number else 'OFF'}.")
        if show_number:
            print("[DEBUG] The number is:", number)

    elif guess == 'm':
        move_mode = not move_mode
        print(f"Move mode {'ON' if move_mode else 'OFF'}.")
    
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

        if move_mode:
            number += random.choice([-2, -1, 0, 1, 2])
            number = max(1, min(20, number)) 
        
        if show_number:
            print("[DEBUG] The number is:", number)
    
    else:
        print("Invalid input. Please enter a number between 1 and 20 or 'x' to exit.")

    guess = input("Enter your guess: ")


print("You have exited the game.")
print("Thanks for playing!")
print("Goodbye")

