def unique_values(dictionary):
    unique_values_set = set()

    for value in dictionary.values():
        unique_values_set.add(value)

    print("Unique values in the dictionary:", list(unique_values_set))


my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
unique_values(my_dict)

