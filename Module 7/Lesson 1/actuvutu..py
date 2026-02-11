from tkinter import *
from datetime import date as dt

root = Tk()
root.title("Simple Calculator")
root.geometry("500x500")

Label(root, text="Number 1", fg="blue", bg="lightgray").pack()
Label(root, text="Number 2", fg="blue", bg="lightgray").pack()
Name_Entry = Entry(root)
Nam2_Entry = Entry(root)

"""

def login():
    global message
    num1 = float(Name_Entry.get())
    num2 = float(Nam2_Entry.get())
    if Addition_Button['state'] == 'active':
        message = Label(root, text=f"Result: {num1 + num2}", fg="green", bg="lightgray")
        message.pack()
    elif Subtraction_Button['state'] == 'active':
        message = Label(root, text=f"Result: {num1 - num2}", fg="green", bg="lightgray")
        message.pack()
    elif Multiplication_Button['state'] == 'active':
        message = Label(root, text=f"Result: {num1 * num2}", fg="green", bg="lightgray")
        message.pack()
    elif Division_Button['state'] == 'active':
        message = Label(root, text=f"Result: {num1 / num2}", fg="green", bg="lightgray")
        message.pack()   

""" 
    
def add():
    num1 = float(Name_Entry.get())
    num2 = float(Nam2_Entry.get())
    message = Label(root, text=f"Result: {num1 + num2}", fg="green", bg="lightgray")
    message.pack()

def subtract():
    num1 = float(Name_Entry.get())
    num2 = float(Nam2_Entry.get())
    message = Label(root, text=f"Result: {num1 - num2}", fg="green", bg="lightgray")
    message.pack()

def multiply():
    num1 = float(Name_Entry.get())
    num2 = float(Nam2_Entry.get())
    message = Label(root, text=f"Result: {num1 * num2}", fg="green", bg="lightgray")
    message.pack()

def divide():
    num1 = float(Name_Entry.get())
    num2 = float(Nam2_Entry.get())
    if num2 != 0:
        message = Label(root, text=f"Result: {num1 / num2}", fg="green", bg="lightgray")
        message.pack()
    else:
        message = Label(root, text="Error: Division by zero is not allowed.", fg="red", bg="lightgray")
        message.pack()

Addition_Button = Button(root, text="Add", command=add)
Subtraction_Button = Button(root, text="Subtract", command=subtract)
Multiplication_Button = Button(root, text="Multiply", command=multiply)
Division_Button = Button(root, text="Divide", command=divide)

Name_Entry.pack()
Nam2_Entry.pack()
Addition_Button.pack()
Subtraction_Button.pack()
Multiplication_Button.pack()
Division_Button.pack()
root.mainloop()