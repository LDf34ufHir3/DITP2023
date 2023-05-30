# GUI Program to create a Text widget using tkinter module

import tkinter as tk

parent = tk.Tk()
# creaate the widget
mytext = tk.Text(parent)

# insert a string at the beginning
mytext.insert('1.0', "-Python exercises, solution -")

# insert a string into the current text
mytext.insert('1.19', 'Practice')

# delete the first and last character (incliuding a newline character)
mytext.delete('1.0')
mytext.delete('end - 2 chars')
mytext.pack()
parent.mainloop()