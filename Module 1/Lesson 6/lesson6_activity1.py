a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if a and b and c:
    print("All variables are true")
elif (a and b) or (b and c) or (a and c):
    print("At least two variables are true")
elif a or b or c:
    print("At least one variable is true")
else:
    print("No variables are true")

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if a > 0 and b > 0 and c > 0:
    print("All variables are positive")
elif (a > 0 and b > 0) or (b > 0 and c > 0) or (a > 0 and c > 0):
    print("At least two variables are positive")
elif a > 0 or b > 0 or c > 0:
    print("At least one variable is positive")
else:
    print("No variables are positive")