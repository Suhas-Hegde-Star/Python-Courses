att = int(input("Enter the attendance: "))
med = input("Do You have medical issue(Type y or n): ")

if med == "y":
    print("You are not allowed to sit in the exam.")
else:
    if att >= 75:
        print("You are allowed to sit in the exam.")
    else:
        print("You are not allowed to sit in the exam.")