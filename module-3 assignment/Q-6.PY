squares = [x**2 for x in range(1, 31)]

# Extract the first and last 5 elements
first_and_last_5 = squares[:5] + squares[-5:]

# Print the result
print("First and last 5 elements of the squares of numbers between 1 and 30:")
print(first_and_last_5)