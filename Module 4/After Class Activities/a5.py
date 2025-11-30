# Take a number from the user create a list with all the odd numbers under the input value and another list of odd numbers above the input value
num = int(input("Enter a number: "))
odd_below = [i for i in range(num) if i % 2 != 0]
odd_above = [i for i in range(num + 1, num + 21) if i % 2 != 0]
print("Odd numbers below", num, ":", odd_below)
print("Odd numbers above", num, ":", odd_above)

# create a list of fruits then convert the first letter of every element to capital and create a new list of updated values
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)