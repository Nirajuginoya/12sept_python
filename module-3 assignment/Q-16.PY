def tuple_to_string(input_tuple):
    string_elements = map(str, input_tuple)
    
    result_string = ''.join(string_elements)
    
    return result_string

my_tuple = (1, 2, 'hello', 3.14)
result = tuple_to_string(my_tuple)

print(f'Tuple: {my_tuple}')
print(f'String: {result}')
