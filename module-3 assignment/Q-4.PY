def is_list_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
    
my_list = [1, 2, 3]
if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")