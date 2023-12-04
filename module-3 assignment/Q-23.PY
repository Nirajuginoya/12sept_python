
def find_repeated_items(tuple_input):
    repeated_items = set()
    unique_items = set()

    for item in tuple_input:
        if item in unique_items:
            repeated_items.add(item)
        else:
            unique_items.add(item)

    return repeated_items

my_tuple = (1, 2, 3, 4, 1, 2, 5, 6, 7, 7, 8)
repeated_items = find_repeated_items(my_tuple)

if repeated_items:
    print("Repeated items in the tuple:", repeated_items)
else:
    print("No repeated items in the tuple.")

