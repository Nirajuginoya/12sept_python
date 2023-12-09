my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys_to_check = ['a', 'c', 'e']

if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Some keys are missing in the dictionary.")

