from tkinter import messagebox, Tk, Button
import random

msgbox = messagebox
r = Tk()
r.title("Virus Alert")
r.geometry("300x200")

button=Button(r, text="Click Me to scan for viruses")
button.pack()

def handle_click(event):
    yesss = msgbox.askyesno("Scanner", "Do you want to scan?")
    if yesss:
        if random.randint(0,1) == 0:
            msgbox.showinfo("Scanner", "Your computer is clean")
        else:
            msgbox.showwarning("Scanner", "Your computer is infected with a virus")
    else:
        msgbox.showinfo("Scanner", "Scan cancelled")

button.bind("<Button-1>", handle_click)
r.mainloop()