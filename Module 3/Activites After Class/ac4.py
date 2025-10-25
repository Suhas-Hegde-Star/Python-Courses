try:
    sss = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")

print("You entered age:", sss)