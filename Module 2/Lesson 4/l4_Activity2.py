nums = int(input("Ener a number : "))
num = nums
lenn = len(str(num))
product = 1

for num in range (1, lenn + 1):
    digit = num % 10
    product *= digit
    num = num // 10

print(product)