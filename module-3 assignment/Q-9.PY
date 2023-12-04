import random

def select_random_item(my_list):
    if not my_list:
        return None  
    else:
        return random.choice(my_list)

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
random_item = select_random_item(my_list)

if random_item is not None:
    print(f"Randomly selected item: {random_item}")
else:
    print("The list is empty.")
