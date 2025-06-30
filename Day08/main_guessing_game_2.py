from number_guessing_game_2_module import generate_number, get_guess, check_guess, is_exit_command

number = generate_number()

print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 20.")
print("You can guess as much as you wish. If you guess the number, you win!")
print("If you want to exit the game, type 'x'")

while True:
    guess_input = get_guess()

    if is_exit_command(guess_input):
        print("You have exited the game.")
        break

    if guess_input.isdigit():
        guess = int(guess_input)
        if check_guess(guess, number):
            print("Thanks for playing!")
            print("Goodbye")
            break
    else:
        print("Invalid input. Please enter a number between 1 and 20 or 'x' to exit.")

