def count_digits_in_list(alist):
    digit_counts = {}
    for d in range(10):
        digit_counts[str(d)] = 0
    for number in alist:
        for digit in str(number):
            if digit in digit_counts:
                digit_counts[digit] += 1

    return digit_counts

user_input = input("Please enter a list of numbers separated by commas: ")
alist = user_input.split(",")

digit_counts = count_digits_in_list(alist)

for digit in sorted(digit_counts.keys()):
    print(f"{digit}  {digit_counts[digit]}")
