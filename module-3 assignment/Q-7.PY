def unique_elements(input_list):
    
    unique_list = list(set(input_list))
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5]
result_list = unique_elements(original_list)
print(result_list)
