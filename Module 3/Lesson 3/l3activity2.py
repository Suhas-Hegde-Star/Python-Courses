string = input("Enter a string: ")
charac = input("Enter a character: ")
index = 0
flag = 0

for i in string:
    if i == charac:
        flag += 1
        break
    index += 1

if flag == 0:
    print("Character not found")
else:
    print("Character found at index:", index)
