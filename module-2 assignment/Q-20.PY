word_list = input("Enter a list of words separated by spaces: ").split()

longest_word = max(word_list, key=len)

length_of_longest_word = len(longest_word)

print("The longest word is:", longest_word)
print("Its length is:", length_of_longest_word)

