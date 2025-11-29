import array as arr

# Create an array of integers
A = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 3, 3, 4, 5, 6])

# Print the original array
print("\n\nOriginal Array:", str(A))

# Number of occurrences of 3 in the array
print ("Count of 3 in array:", str(A.count(3)))

# Reverse the array
print("Reversed Array:", str(A[::-1]))