import random

def get_random_number():
    return random.randint(1, 20)

number = get_random_number()
show_number = False 
move_mode = False 

print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 20.")
print("You can guess as much as you wish. If you guess the number, you win!")
print("Type 'x' to exit the game.")
print("Type 'd' to toggle debug mode (show number).")
print("Type 'm' to toggle move mode (number may shift slightly).")
print("Type 'n' to start a new game (new number).") 

while True:
    guess = input("Enter your guess: ")

    if guess.lower() == 'x':
        print("You have exited the game.")
        break

    elif guess.lower() == 'd':
        show_number = not show_number
        print(f"Debug mode {'ON' if show_number else 'OFF'}.")
        if show_number:
            print(f"(Number is: {number})")

    elif guess.lower() == 'm':
        move_mode = not move_mode
        print(f"Move mode {'ON' if move_mode else 'OFF'}.")

    elif guess.lower() == 'n':
        number = get_random_number()
        print("Starting a new game! I picked a new number.")
        if show_number:
            print(f"(Number is: {number})")

    elif guess.isdigit():
        guess = int(guess)
        if guess > number:
            print("Sorry, you guessed too high. Try again.")
        elif guess < number:
            print("Sorry, you guessed too low. Try again.")
        else:
            print("Congratulations! You guessed the number!")
            print("Starting a new game!") 
            number = get_random_number()

        if move_mode:
            shift = random.randint(-2, 2)
            number = max(1, min(20, number + shift))

        if show_number:
            print(f"(Number is: {number})")

    else:
        print("Invalid input. Please enter a number between 1 and 20 or a valid command (x, d, m, n).")
        
print("Thanks for playing!")
print("Goodbye!")
