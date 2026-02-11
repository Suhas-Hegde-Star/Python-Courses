from tkinter import *
from datetime import date as dt

root = Tk()
root.title("Login to Website")
root.geometry("400x300")

Label(root, text="Username", fg="blue", bg="lightgray").pack()
Label(root, text="Password", fg="blue", bg="lightgray").pack()
Name_Entry = Entry(root)
Password_Entry = Entry(root, show="*")

def login():
    username = Name_Entry.get()
    global message
    message = Label(root, text="Login Successful!", fg="green", bg="lightgray")
    message.pack()
    greet = Label(root, text=f"Welcome, {username}!", fg="blue", bg="lightgray")
    greet.pack()
    today = dt.today()
    date_label = Label(root, text=f"Today's date: {today}", fg="purple", bg="lightgray")
    date_label.pack()
    
Login_Button = Button(root, text="Login", command=login)

Name_Entry.pack()
Password_Entry.pack()
Login_Button.pack()
root.mainloop()