set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union Of Sets
set3 = set1.union(set2)
print("Union :", set3)

# Intersection Of Sets
set3 = set1.intersection(set2)
print("Intersection :", set3)

# Difference Of Sets
set3 = set1.difference(set2)
print("Difference :", set3)

# Difference Of Sets
set3 = set2.difference(set1)
print("Difference :", set3)

# Symetrical Difference Of Sets
set3 = set1.symmetric_difference(set2)
print("Symmetrical Difference :", set3)

# Symetrical Difference Of Sets
set3 = set2.symmetric_difference(set1)
print("Symmetrical Difference :", set3)