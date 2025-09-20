limit = int(input("Enter the limit: "))

for num in range(1, limit + 1):
    powe = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** powe
        temp //= 10

    if sum == num:
        print(sum,"is an Armstrong Number")