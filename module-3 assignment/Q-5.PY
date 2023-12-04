lists = [1, 2, 3, 4, 5]
another_list = [5, 6, 7, 8, 9]

# Without using a function definition
common_member = any(item in lists for item in another_list)

# Print the result
print(common_member)