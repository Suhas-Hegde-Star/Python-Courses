a = int(input("Enter a speed of cyclist: "))
b = int(input("Enter another speed of cyclist: "))
c = int(input("Enter one more speed of cyclist: "))

av = (a + b + c) / 3
print("The average speed of the cyclists is:", av)

if a > av:
    print("The first cyclist is faster than the average.")
elif b > av:
    print("The second cyclist is faster than the average.")
elif c > av:
    print("The third cyclist is faster than the average.")

if a < av:
    print("The first cyclist is slower than the average.")
if b < av:
    print("The second cyclist is slower than the average.")
elif c < av:
    print("The third cyclist is slower than the average.")


if a == av:
    print("The first cyclist is at the average speed.")
elif b == av:
    print("The second cyclist is at the average speed.")
elif c == av:
    print("The third cyclist is at the average speed.")