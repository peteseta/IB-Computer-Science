from tkinter import *

root = Tk()
root.title("Morse Code Encoder")
root.geometry("400x200")


char_to_dots = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": " ",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}

# encodes the morse
def encode_morse(s):
    return " ".join(char_to_dots[char.upper()] for char in s.replace(" ", ""))


# encode the text in the entry and update the label stringvar
def update_label(*args):
    output.set(encode_morse(input.get()))


input = StringVar()
output = StringVar()

# when the entry box is changed, call encode()
input.trace_add("write", update_label)

t = Label(text="Enter text to encode:")
t.pack()

e = Entry(textvariable=input)
e.pack()

l = Label(textvariable=output, wraplength=350)
l.pack()

b = Button(
    text="Copy to clipboard",
    command=lambda: root.clipboard_clear() or root.clipboard_append(output.get()),
)
b.pack()

root.mainloop()
