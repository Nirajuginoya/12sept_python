def concatenate_dicts(dict1, dict2, dict3):
    
    concatenated_dict = dict1.copy()
    concatenated_dict.update(dict2)
    concatenated_dict.update(dict3)


    return concatenated_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

result_dict = concatenate_dicts(dict1, dict2, dict3)

print("Concatenated Dictionary:", result_dict)
