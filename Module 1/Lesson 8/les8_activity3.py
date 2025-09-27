num = int(input("Enter a number: "))
x = int(input("Enter another number: "))

if num % x == 0:
    print(num, "is divisible by", x)
else:
    print(num, "is not divisible by", x)