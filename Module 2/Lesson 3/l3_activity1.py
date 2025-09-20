n = int(input("Enter a number "))
h = n
sum = 0

while n > 0:
    sum += n
    n -= 1

print ("The sum of numbers till {} is {}".format(h, sum))