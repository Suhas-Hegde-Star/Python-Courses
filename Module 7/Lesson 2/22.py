from tkinter import *

r = Tk()
r.title("Login Form")
r.geometry("400x400")
frame = Frame(r, relief=SOLID, height=200, width=360, borderwidth=6.7)

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
    msg1 = "You have entered the following details to login:"
    msg2 = f"Hi {name_entry.get()},"
    msg3 = f"Your Phone Number is {phone_entry.get()}"
    msg4 = f"You have registered with the email ID: {email_entry.get()}"
    msg5 = f"Your password is {password_entry.get()}"
    label_msg1 = Label(frame, text=msg1)
    label_msg2 = Label(frame, text=msg2)
    label_msg3 = Label(frame, text=msg3)
    label_msg4 = Label(frame, text=msg4)
    label_msg5 = Label(frame, text=msg5)
    label_msg1.pack(padx=5, pady=5)
    label_msg2.pack(padx=5, pady=5)
    label_msg3.pack(padx=5, pady=5)
    label_msg4.pack(padx=5, pady=5)
    label_msg5.pack(padx=5, pady=5)

frame.pack(padx=10, pady=10)
label1.pack(padx=5, pady=5)
name_entry.pack(padx=5, pady=5)
label2.pack(padx=5, pady=5)
phone_entry.pack(padx=5, pady=5)
label3.pack(padx=5, pady=5)
email_entry.pack(padx=5, pady=5)
label4.pack(padx=5, pady=5)
password_entry.pack(padx=5, pady=5)
login_button = Button(frame, text="Login", command=display)
login_button.pack(padx=5, pady=5)

r.mainloop()