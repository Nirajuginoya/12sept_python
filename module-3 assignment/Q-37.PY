from collections import defaultdict

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = defaultdict(int)

for entry in data:
    result[entry['item']] += entry['amount']

print(dict(result))

