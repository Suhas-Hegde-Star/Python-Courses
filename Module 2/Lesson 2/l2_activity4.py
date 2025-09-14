num1 = int(input("Enter a number"))

for num in range (2, num1+1):
    prime = True
    if num1 <= 1:
        prime = False
        break
    else:
        for i in range (2, num):
            if num % i == 0:
                prime = False
    if prime:
        print(prime, num, "is a prime number") 