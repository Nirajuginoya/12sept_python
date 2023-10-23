string =input("enter a string:")
string_to_insert = input("enter a string:")

middle = len(string) // 2
new_string = string[:middle] + string_to_insert + string[middle:]

print(new_string)