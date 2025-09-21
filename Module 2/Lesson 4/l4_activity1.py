count = 0
i = 0

string = input("Enter sentence: ")
charac = input("Enter a letter: ")

while i < len(string):
    if string[i] == charac:
        count += 1
    i += 1

print("The amount of times ihe letter \"" + charac + "\" occours in \"" + string + "\" is", count)
