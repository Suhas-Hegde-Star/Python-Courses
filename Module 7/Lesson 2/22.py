from tkinter import *

r = Tk()
r.title("Login Form")
r.geometry("400x400")
frame = Frame(r, relief=SOLID, height=200, width=360, borderwidth=6.7)

label1 = Label(frame, text="Full Name (In Capital letters only)")
label2 = Label(frame, text="Phone Number (10 digit only)")
label3 = Label(frame, text="Email ID (must contain @ and .com only)")
label4 = Label(frame, text="Password (must contain set password)")
label5 = Label(frame, text="Confirm Password (must match set password)")

name_entry = Entry(frame)
phone_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="#")
confirm_password_entry = Entry(frame, show="+-*/")

r.mainloop()