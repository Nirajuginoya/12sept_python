lists = [1, 2, 3, 4, 5]
another_list = [5, 6, 7, 8, 9]

common_member = any(item in lists for item in another_list)

print(common_member)