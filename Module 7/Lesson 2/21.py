from tkinter import *

r = Tk()
r.title("Number Pad")
r.geometry("400x400")
number = [    [9, 8, 7],     [6, 5, 4],     [3, 2, 1],     ["#", 0, "><"]    ]

for i in range(4):
    r.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        r.columnconfigure(j, weight=1, minsize=50)
        frame = Frame(r, relief=SOLID, borderwidth=6.7)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = Label(frame, text=number[i][j])
        label.pack( padx=5, pady=5)

r.mainloop()