from tkinter import *
import math

r = Tk()
r.title("Inches to Centimeters")
r.geometry("300x300")
Label(r, text="Enter length in inches", fg="blue", bg="lightgray").pack()
entry = Entry(r)
entry.pack()

result_label = Label(r, text="")
result_label.pack()

def convert():
    inches = entry.get()
    centimeters = inches * 2.54
    result_label.config(text=f"{inches} inches is equal to {centimeters} centimeters.")

Button(r, text="Convert", command=convert).pack()
r.mainloop()