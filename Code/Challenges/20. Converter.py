from tkinter import *

root = Tk()
root.title("Code Encoder/Decoder")
root.geometry("400x200")

morse_dict = {
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

# encodes to morse
def text_to_morse(s):
    return " ".join(morse_dict[char.upper()] for char in s.replace(" ", ""))


# encode to ordinal
def text_to_ord(s):
    return " ".join(str(ord(char)) for char in s)


# decode morse code to text
def morse_to_text(s):
    text = ""
    for char in s.split(" "):
        for dot in morse_dict:
            if morse_dict[dot] == char:
                text += dot
    return text


# decode ordinal to text
def ordinal_to_text(s):
    return "".join(chr(int(char)) for char in s.split(" "))


input = StringVar()
output = StringVar()

t = Label(text="Enter text to encode:")
t.pack()

e = Entry(textvariable=input)
e.pack()

l = Label(textvariable=output, wraplength=350)
l.pack()

b_morse = Button(
    text="Convert Text to Morse",
    command=lambda: output.set(text_to_morse(input.get())),
)
b_morse.pack()

b_ordinal = Button(
    text="Convert Text to Ordinal",
    command=lambda: output.set(text_to_ord(input.get())),
)
b_ordinal.pack()

b_to_morse = Button(
    text="Convert Morse to Text",
    command=lambda: output.set(morse_to_text(input.get())),
)
b_to_morse.pack()

b_to_ordinal = Button(
    text="Convert Ordinal to Text",
    command=lambda: output.set(ordinal_to_text(input.get())),
)
b_to_ordinal.pack()

root.mainloop()
