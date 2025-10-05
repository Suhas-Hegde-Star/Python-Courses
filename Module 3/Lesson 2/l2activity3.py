def factorial(x):
    """
    This Function is used to find the Factorial of a particular number.
    """
    if x == 1 or 0:
        return 1
    else:
        return x * factorial(x-1)
    
inp = int(input("Enter a Number: "))
print(factorial.__doc__)

while inp != 0:
    print(factorial(inp))
    inp -= 1