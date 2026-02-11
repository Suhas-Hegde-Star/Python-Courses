import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.geometry("400x300")
label = tk.Label(window, text="Hello, World!")
label.pack()
window.mainloop()