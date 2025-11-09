# Create a tuple containing 4 data types
tuple1 = ("Hi", 1, 12.34, True)
print(tuple1)

# Create a tuple with numbers
tuple2 = (10, 20, 30, 40, 50)
print(tuple2)

# Add Element to a Tuple via making a new tuple
element = int(input("Enter a number to add to the tuple: "))
new_tuple = tuple2 + (element,)
print(new_tuple)

# Search the number of times a number appears in the number tuple
search_num = int(input("Enter a number to search in the tuple: "))
print(f"The number {search_num} appears {new_tuple.count(search_num)} times in the tuple.")