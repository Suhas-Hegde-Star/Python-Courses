def cube(x):
    return x^3

def d(y):
    if y % 3 == 0:
        return cube(y)
    else:
        return False
    
print(d(100),d(99),d(101010101))