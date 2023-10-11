from tkinter import *

windown = Tk()
windown.title("Grid Example UI")
windown.minsize(width=450, height=600)

# label
label = Label(text="Enter a text", font=('Fira code', 15, 'bold'))
label.grid(row=0, column=0)

# Button
def button_click():
    pass

button = Button(text="Click me", command=button_click)
button.grid(column=1, row=1)

# Entry
input = Entry()
input.grid(row=2, column=2)

windown.mainloop()