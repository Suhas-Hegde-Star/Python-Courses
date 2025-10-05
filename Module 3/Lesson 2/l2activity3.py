def factorial(x):
    """\
This Function is used to find the Factorial of a particular number.\
    """
    if x == 1 or 0:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial.__doc__)
print(factorial(10))
print(factorial(5))