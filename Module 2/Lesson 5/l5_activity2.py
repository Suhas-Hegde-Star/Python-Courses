num = int(input("Enter a number: "))
n = 1

print("Floyd's Triangle:")
nu = num + 1
for i in range(nu):
    for j in range(i + 1):
        print(n, end= " ")
        n += 1
    print()