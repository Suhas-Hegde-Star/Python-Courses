a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

print (a != b)
print (b != c)
print (a != c)

a = str(input("Enter a word: "))
b = str(input("Enter a second word: "))

if a != b:
    print("The words are different")
else:
    print("The words are the same")

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))

if (a == 4) != (b == 4):
    print("At least two numbers are equal to 4")
else:
    print("All numbers are different and not equal to 4")
