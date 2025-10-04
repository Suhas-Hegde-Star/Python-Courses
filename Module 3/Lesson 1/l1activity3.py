def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

o = input("Enter the operation to do(Type the number): \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

if o == "1":
    add(n1, n2)
elif o == "2":
    sub(n1, n2)
elif o == "3":
    mul(n1, n2)
elif o == "4":
    div(n1, n2)
else:
    print("Invalid Input. Try With Numbers.")
    oo = input("Enter the operation to do(Type the number): \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
    if oo == "1":
        add(n1, n2)
    elif oo == "2":
        sub(n1, n2)
    elif oo == "3":
        mul(n1, n2)
    elif oo == "4":
        div(n1, n2)
    else:
        print("Invalid Input. Try With Numbers properly.")
        ooo = input("Enter the operation to do(Type the number): \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
        if ooo == "1":
            add(n1, n2)
        elif ooo == "2":
            sub(n1, n2)
        elif ooo == "3":
            mul(n1, n2)
        elif ooo == "4":
            div(n1, n2)
        else:
            print("Invalid Input. Bye")