from tkinter import *
import datetime

r = Tk()
r.title("Age Calculator")
r.geometry("300x300")
birth_Entry = Label(r, text="Enter your birth year", fg="blue", bg="lightgray")
entry = Entry(r)
birth_Entry.pack()
entry.pack()

result_label = Label(r, text="")
result_label.pack()

def calculate_age():
    birth_year = int(entry.get())
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    result_label.config(text=f"You are {age} years old.")

Button(r, text="Calculate Age", command=calculate_age).pack()
r.mainloop()