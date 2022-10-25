from tkinter import *

root = Tk()

var = StringVar()
var.set("Awaiting calculation...")


def on_click():
    var.set(str(calculate(str(input.get()))))


def calculate(input):
    # append each number found in the input to a list
    numbers = []
    current_number = ""
    for i in input:
        if i.isdigit():
            current_number += i
        else:
            # if there is a number, append it
            if current_number:
                numbers.append(int(current_number))
                current_number = ""
    # if there is a number left over, append it
    if current_number:
        numbers.append(int(current_number))

    return sum(numbers)


# make input box in tkinter
input = Entry(root, text="Calculation:")
input.pack()

# make button in tkinter
button = Button(root, text="Calculate", command=on_click)
button.pack()

label = Label(root, textvariable=var)
label.pack()

root.mainloop()
