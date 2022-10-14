from tkinter import *

root = Tk()

a = Label(root, text="Choose a greeting...")
a.pack()

greetings = ("Hi there!", "Hello!", "Howdy!", "Greetings!", "Sup!")

var = Variable(value=greetings)
listbox = Listbox(root, listvariable=var)
listbox.pack()


def buttonGreeting():
    print(listbox.get(listbox.curselection()))


b = Button(root, text="Click me", command=buttonGreeting)
b.pack()

root.mainloop()
