import tkinter as tk
from tkinter import messagebox
def show_message():
    messagebox.showinfo("Message", "This is a simple tkinter window!")

root = tk.Tk()
root.title("Simple tkinter App")

btn = tk.Button(root, text="Click Me", command=show_message)
btn.pack(pady=20)

root.mainloop()