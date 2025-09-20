n = input("Enter a number ")
powe = len(n)
sum = 0
n = int(n)
temp = int(n)


while temp > 0:
    digit = temp % 10
    sum += digit ** powe
    temp //= 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstog number")