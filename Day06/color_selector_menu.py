
import sys

colors = ["blue", "green", "yellow", "white"]

def print_menu():
    print("Please select a color:")
    i = 1
    for color in colors:
        print(str(i) + ". " + color)
        i = i + 1

def get_user_choice():
    while True:
        print_menu()
        user_input = input("Enter the number of your choice: ")

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(colors):
                return choice
            else:
                print("Error: Number is out of range. Please try again.")
        else:
            print("Error: Please enter a valid number.")

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg.isdigit():
            choice = int(arg)
            if 1 <= choice <= len(colors):
                print("You selected:", colors[choice - 1])
                return
            else:
                print("Number out of range. Showing menu instead.")
        else:
            arg_lower = arg.lower()
            if arg_lower in colors:
                print("You selected:", arg_lower)
                return
            else:
                print("Color not found. Showing menu instead.")

    selected_number = get_user_choice()
    print("You selected:", colors[selected_number - 1])

main()
