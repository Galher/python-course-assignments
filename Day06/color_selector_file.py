
file_path = input("Enter the path to your color file: ").strip('"')

colors = []

try:
    with open(file_path, "r") as file:
        for line in file:
            color = line.strip()
            if color: 
                colors.append(color)
except FileNotFoundError:
    print("Error: File not found.")
    exit()

print("Please select a color:")
i = 1
for color in colors:
    print(str(i) + ". " + color)
    i = i + 1

while True:
    choice = input("Enter the number of your choice: ")
    if choice.isdigit():
        number = int(choice)
        if number >= 1 and number <= len(colors):
            selected_color = colors[number - 1]
            print("You selected:", selected_color)
            break
        else:
            print("Error: Number is out of range.")
    else:
        print("Error: Please enter a valid number.")
