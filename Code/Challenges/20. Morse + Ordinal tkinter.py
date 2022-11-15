from tkinter import *

root = Tk()
root.title("Morse Code Encoder")
root.geometry("400x200")

# encodes to morse
def encode_morse(s):
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
    return " ".join(char_to_dots[char.upper()] for char in s.replace(" ", ""))


# encode to ordinal
def encode_ord(s):
    return " ".join(str(ord(char)) for char in s)


# encode the text in the entry and update the label stringvar
def update_label(*args):
    morse_output.set(encode_morse(input.get()))
    ordinal_output.set(encode_ord(input.get()))


input = StringVar()
morse_output = StringVar()
ordinal_output = StringVar()

# when the entry box is changed, call encode()
input.trace_add("write", update_label)

t = Label(text="Enter text to encode:")
t.pack()

e = Entry(textvariable=input)
e.pack()

l_m = Label(textvariable=morse_output, wraplength=350)
l_m.pack()

l_o = Label(textvariable=ordinal_output, wraplength=350)
l_o.pack()

b_m = Button(
    text="Copy morse to clipboard",
    command=lambda: root.clipboard_clear() or root.clipboard_append(morse_output.get()),
)
b_m.pack()

b_o = Button(
    text="Copy ordinal to clipboard",
    command=lambda: root.clipboard_clear()
    or root.clipboard_append(ordinal_output.get()),
)
b_o.pack()

root.mainloop()
