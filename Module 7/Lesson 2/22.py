from tkinter import *

r = Tk()
r.title("Login Form")
r.geometry("400x400")
frame = Frame(r, relief=GROOVE, height=200, width=360, borderwidth=6.7)

label1 = Label(frame, text="Full Name (In letters only)")
label2 = Label(frame, text="Phone Number (10 digit only)")
label3 = Label(frame, text="Email ID (must contain @ and .com only)")
label4 = Label(frame, text="Password (must contain set password)")

name_entry = Entry(frame)
phone_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="#")
confirm_password_entry = Entry(frame, show="+-*/")

def display():
    print("You have entered the following details to login:")
    print("Hi ", name_entry.get(), ",")
    print("Your Phone Number is ", phone_entry.get())
    print("You have registered with the email ID:", email_entry.get())
    print("Your password is", password_entry.get())

frame.pack(padx=10, pady=10)
label1.pack(padx=5, pady=5)
name_entry.pack(padx=5, pady=5)
label2.pack(padx=5, pady=5)
if len(phone_entry.get()) != 10:
    print("Please enter a valid 10 digit phone number.")
else:
    phone_entry.pack(padx=5, pady=5)
label3.pack(padx=5, pady=5)
email_entry.pack(padx=5, pady=5)
label4.pack(padx=5, pady=5)
password_entry.pack(padx=5, pady=5)
login_button = Button(frame, text="Login", command=display)
login_button.pack(padx=5, pady=5)

r.mainloop()