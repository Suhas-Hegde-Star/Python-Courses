count = 0
start = 0 

string = input("Enter sentence: ")
charac = input("Enter a letter: ")
letter = len(charac)
end = letter

while end < len(string):
    if string[start:end] == charac:
        count += 1
    end += 1
    start += 1

print("The amount of times ihe letter \"" + charac + "\" occours in \n\"" + string + "\n\" is", count)
