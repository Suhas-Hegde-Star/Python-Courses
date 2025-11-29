from collections import Counter

# Example dictionary
my_dict = {'a': 3, 'b': 3, 'c': 2, 'd': 5}

# Count frequency of each value
value_freq = Counter(my_dict.values())

print(value_freq)
