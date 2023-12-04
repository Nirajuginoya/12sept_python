my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending Order:", sorted_dict_asc)
print("Descending Order:", sorted_dict_desc)
