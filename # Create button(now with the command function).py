from tkinter import * # imports everything from TK

root = Tk() # top level window

def callback():
    label.config(text='You clicked me!', fg='red', bg='yellow')
# Here I have added font colour and background colour on click

# Create Label
label = Label(root, text="Hello Python")
label.pack()

# Create button(now with the command function)
button = Button(root, text='Click me!', command=callback)
button['state'] = 'disabled' # can disable the button
button['state'] = 'normal' # back to normal
button.pack()

root.geometry("350x300")
root.mainloop