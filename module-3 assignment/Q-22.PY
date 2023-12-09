tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_value = 10
for i in range(len(tuple_list)):
    tuple_list[i] = tuple_list[i][: -1] + (new_value,)

print(tuple_list)