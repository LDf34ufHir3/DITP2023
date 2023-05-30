# GUI program to create a Combobox with three options using tkinter

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_str_var = tk.StringVar()

my_combobox = ttk.Combobox(
    root, textvariable=my_str_var,
    values=["PHP", "Java", "Python"])

my_combobox2 = ttk.Combobox(
    root, textvariable=my_str_var,
    values=["A1", "B2", "C3"])

my_combobox.pack()
root.mainloop()