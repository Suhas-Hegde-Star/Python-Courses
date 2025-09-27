char = input("Enter a character: ")
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")

text = input("Enter a string: ")
ascii_values = [ord(c) for c in text]
print(ascii_values)