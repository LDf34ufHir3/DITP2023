from tkinter import * # imports everything from TK - tkinter is a module
from tkinter import ttk # ttk is a sub module of tkinter

root = Tk() # top level window

# Create a Label Widget
label= Label(root, text="Hello Python") # What you see on screen

# font colour, config is for proerties
label.config(text="Hello Python",borderwidth=1,relief="solid",font="Times 32")
label.config(bg="orange") # Background colour 
label.config(font='Times 20')

label.config(text='Python is a great program and we can do lots with it.')
label.config(wraplength='150') # wrap a text if long label
label.config(justify="right")

# Showing it on screen
label.pack()
root.geometry("300x250")

root.mainloop() # GUI is looping - when you run your mouse over an you can click on any buttons/labels
