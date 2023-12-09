from itertools import product

def display_combinations(dictionary):
    keys = list(dictionary.keys())
    combinations = product(*[dictionary[key] for key in keys])

    for combo in combinations:
        print(' '.join(combo))

sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}

display_combinations(sample_data)
