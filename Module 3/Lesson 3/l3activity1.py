def function_of_a_function(list):
    """
    This is a docstring. It explains what the function does.
    """
    flag = 0
    for num in list:
        if num < 0:
            continue
        elif num == 0:
            pass
        elif (num % 7 == 0) and (num % 2 == 0):
            flag = 1
            break
    if flag == 1:
        return num
    else:
        return "No such number found"

x = []

for i in range(101):
    x.append(i + 1)

print(function_of_a_function(x))