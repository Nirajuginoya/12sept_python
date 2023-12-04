main_list = [1, 2, 3, 4, 5, 6, 7, 8]

sub_list = [3, 4, 5]

if all(item in main_list for item in sub_list):
    print("Sublist found in the main list")
else:
    print("Sublist not found in the main list")
