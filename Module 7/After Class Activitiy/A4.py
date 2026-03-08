# Write a Python program to create an application to take inputs of the principal amount, time period, and rate of interest from the user, and return the simple interest and compound interest on the same principle using the Python Tkinter library.

from tkinter import *

r = Tk()
r.title("Interest Calculator")
r.geometry("400x400")
Label(r, text="Principal Amount").pack()
principal_entry = Entry(r)
principal_entry.pack()
Label(r, text="Time Period (years)").pack()
time_entry = Entry(r)
time_entry.pack()
Label(r, text="Rate of Interest (%)").pack()
rate_entry = Entry(r)
rate_entry.pack()
result_label = Label(r, text="")
result_label.pack()
def calculate():
    principal = float(principal_entry.get())
    time = float(time_entry.get())
    rate = float(rate_entry.get())
    
    simple_interest = (principal * time * rate) / 100
    compound_interest = principal * (1 + rate / 100) ** time - principal
    
    result_label.config(text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")
Button(r, text="Calculate", command=calculate).pack()
r.mainloop()