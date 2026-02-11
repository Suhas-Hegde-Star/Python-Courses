from tkinter import *

window = Tk()
window.title("My First GUI")
window.geometry("400x300")
label = Label(window, text="Hello, World!")
label.pack()
window.mainloop()