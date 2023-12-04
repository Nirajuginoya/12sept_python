string_list = ["abc", "level", "hello", "radar", "python", "noon"]

count = 0
for word in string_list:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("Number of strings where the first and last character are the same:", count)