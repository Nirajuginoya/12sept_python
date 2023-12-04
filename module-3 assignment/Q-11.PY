def get_unique_values(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
result = get_unique_values(my_list)
print(result)