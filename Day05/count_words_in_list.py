def count_words_in_list(wlist):
    words_counts = {}
    for word in wlist:
        if word not in words_counts:
            words_counts[word] = 1
        else:
            words_counts[word] += 1
    return words_counts

user_input = input("Please enter a list of words separated by commas: ")
wlist = user_input.split(",")

words_counts = count_words_in_list(wlist)

for word in sorted(words_counts.keys()):
    print(f"{word}  {words_counts[word]}")