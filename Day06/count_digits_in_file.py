input_path = input("Enter the path to your text file: ").strip('"')


digit_counts = [0] * 10

with open(input_path, 'r') as file:
    for line in file:
        for char in line:
            if char.isdigit():
                digit = int(char)
                digit_counts[digit] += 1

with open('report.txt', 'w') as report:
    for i in range(10):
        report.write(str(i) + ' ' + str(digit_counts[i]) + '\n')

print("Done! Results saved to report.txt")