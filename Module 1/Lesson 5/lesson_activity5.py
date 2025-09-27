import os

def encrypt(x):
    if x == "1":
        return "!"
    elif x == "2":
        return "@"
    elif x == "3":
        return "#"
    elif x == "4":
        return "$"
    elif x == "5":
        return "%"
    elif x == "6":
        return "^"
    elif x == "7":
        return "&"
    elif x == "8":
        return "*"
    elif x == "9":
        return "~"
    else:
        return "]"

print ("Create Your Login Details")
username = input("Enter a username: ")
password = input("Enter a password: ")

new_password = ""
for char in password:
    new_password += encrypt(char)
    password = new_password

os.system('cls')

print("Enter Your Login Details")
usernamee = input("Username: ")
passworde = input("Password: ")

new_password2 = ""
for char in passworde:
    new_password2 += encrypt(char)
    password2 = new_password2

if usernamee == username and password2 == password:
    print("Login successful!")
else:
    print("Login failed.")