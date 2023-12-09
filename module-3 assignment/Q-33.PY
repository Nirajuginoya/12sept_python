from collections import Counter

def combine_dictionaries(d1, d2):
    result = Counter(d1) + Counter(d2)
    return result

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = combine_dictionaries(d1, d2)

print(combined_dict)