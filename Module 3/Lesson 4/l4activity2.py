import datetime

one = str(datetime.datetime.now())
log = []

try:
    num1, num2 = eval(input("Enter two numbers separated by comma: "))
    result = num1 / num2
    print("The result of division is:", result)
    log.append(one + " : Division Successful")
    log.append("\n")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    log.append(one + " : Division by Zero Error")
    log.append("\n")
except SyntaxError:
    print("Error: Invalid input format. Please enter two numbers separated by a comma.")
    log.append(one + " : Syntax Error")
    log.append("\n")
except ValueError:
    print("Error: Please enter valid numbers.")
    log.append(one + " : Value Error")
    log.append("\n")
except :
    print("An unexpected error occurred.")
    log.append(one + " : Unexpected Error")
    log.append("\n")
else:
    print("No errors occurred.")
finally:
    print("Code completed.")

with open("log2.txt", "a") as f:
    f.writelines(log)