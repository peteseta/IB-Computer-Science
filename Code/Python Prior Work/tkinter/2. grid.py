# testing tkinter
from tkinter import *

# init?
root = Tk()

# labels created
myLabel1 = Label(root, text="hello world")
myLabel2 = Label(root, text="my name is the computer")

# putting label on screen
# grid: putting the label in a grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# continuously looping
root.mainloop()
