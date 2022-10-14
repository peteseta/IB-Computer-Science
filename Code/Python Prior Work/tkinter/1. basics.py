# testing tkinter 
from tkinter import *

# init?
root = Tk()

# label created
myLabel = Label(root, text="hello world")

## putting label on screen
# pack: shoving the label wherever it can go
myLabel.pack()

# continuously looping
root.mainloop()
