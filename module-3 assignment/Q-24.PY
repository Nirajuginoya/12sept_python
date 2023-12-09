def remove_empty_tuples(tuple_list):
   
    filtered_list = [t for t in tuple_list if t]
    return filtered_list

list_of_tuples = [(1, 2, 3), (), (4, 5), (), (6,), ()]
result = remove_empty_tuples(list_of_tuples)

print("Original list of tuples:", list_of_tuples)
print("List after removing empty tuples:", result)