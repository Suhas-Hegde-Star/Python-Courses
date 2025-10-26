numbers = []


for i in range(1, 101):
    numbers.append(i)

sum = 0
for number in numbers:
    sum += number

print(f"The Sum of all numbers is {sum}")
print("The Average is", sum / len(numbers))
print("The Maximum number is", max(numbers))
print("The Minimum number is", min(numbers))