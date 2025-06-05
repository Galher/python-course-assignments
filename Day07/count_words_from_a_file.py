input_filename = input("Enter the name of the file to read: ")

output_filename = "words_and_spaces_counted.txt"

try:
    file = open(input_filename, 'r', encoding='utf-8')
    text = file.read()
    file.close()

    words = text.split()
    word_counts = {}

    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.keys())

    output_file = open(output_filename, 'w', encoding='utf-8')

    for word in sorted_words:
        count = word_counts[word]
        output_file.write(word + " " + str(count) + "\n")

    output_file.close()
    print("Word counts saved to", output_filename)

except FileNotFoundError:
    print("Error: File '" + input_filename + "' not found.")
except Exception as e:
    print("An error occurred: " + str(e))
