from tkinter import *
from random import choice

root = Tk()
root.title("Morse Code Game")
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

char = StringVar(root)
answer = StringVar(root)
score = StringVar(root, "Score: 0")

# pick a random letter from the dictionary
def random_morse():
    global ref_char
    while ref_char := choice(list(morse_dict.keys())):
        if ref_char == " ":
            continue
        else:
            return morse_dict[ref_char]


def generate():
    global morse_char
    global ref_char

    morse_char = random_morse()
    print(f"{ref_char} is {morse_char}")
    char.set(morse_char)


def check():
    global ref_char
    if answer.get().upper() == ref_char:
        answer_label.configure(text="Correct!", bg="green")
        score.set("Score: " + str(int(score.get().split(" ")[1]) + 1))
    else:
        exit()


char_label = Label(root, textvariable=char)
char_label.grid(row=0, column=0)

answer_label = Label(root, text="Enter your answer:")
answer_label.grid(row=1, column=0)

entry = Entry(root, textvariable=answer)
entry.grid(row=1, column=1)

generate = Button(root, text="New Character", command=generate)
generate.grid(row=2, column=0)

check = Button(root, text="Check Answer", command=check)
check.grid(row=3, column=0)

scoreL = Label(root, textvariable=score)
scoreL.grid(row=4, column=0)

root.mainloop()
