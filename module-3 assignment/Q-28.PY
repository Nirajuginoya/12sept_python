def check_key(dictionary, key):
    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

my_dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}
check_key(my_dictionary, 'age') 
check_key(my_dictionary, 'gender')