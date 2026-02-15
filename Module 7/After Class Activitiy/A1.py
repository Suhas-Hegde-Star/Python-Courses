from tkinter import *
from datetime import date as dt

from numpy import divide

root = Tk()
root.title("Simple Calculator")
root.geometry("500x500")

Label(root, text="Number 1", fg="blue", bg="lightgray").pack()
Label(root, text="Number 2", fg="blue", bg="lightgray").pack()
Name_Entry = Entry(root)
Nam2_Entry = Entry(root)

def multiply():
    num1 = float(Name_Entry.get())
    num2 = float(Nam2_Entry.get())
    message = Label(root, text=f"Result: {num1 * num2}", fg="green", bg="lightgray")
    message.pack()

Multiplication_Button = Button(root, text="Multiply", command=multiply)

Name_Entry.pack()
Nam2_Entry.pack()
Multiplication_Button.pack()
root.mainloop()