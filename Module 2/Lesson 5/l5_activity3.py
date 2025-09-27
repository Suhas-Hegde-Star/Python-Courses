row = int(input("Enter the number of rows for Diamond: "))
if row % 2 == 0:
    half = int(row / 2)
else:
    half = int(row / 2 + 1)

s = half - 1
for i in range(1,half + 1):
    for j in range(1, s + 1):
        print(" ", end="")
    s -= 1
    num = 1
    for k in range(2 * i - 1):
        print(num, end="")
        num += 1   
    print()

s = 1
num = 1

for i in range(half - 1,):
    for j in range(s + 1):
        print(" ", end="")
    s = 1
    for k in range(1, 2 * (half - i)):
        print(num, end="")
        num += 1
    print()