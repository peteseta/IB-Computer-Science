# create a simon memory game
# it will have 4 panels which flash colors for the user to remember and then repeat
# on the first round, flash 1 color. each subsequent round, increase the number of colors flashed.
# GUI is created using tkinter. It has 4 buttons, each with a different color: red, green, blue, yellow
# you will also need a button to start a new game and a field for score from the last round

from tkinter import *
from tkmacosx import Button
import random
from functools import partial

# init the window
root = Tk()
root.title("Simon Memory Game")

# init buttons in a loop
colors = ["red", "green", "blue", "yellow"]

# times to flash
level = 5
seq_pos = 0
flash_sequence = []

# clear sequence and flash
def start_game():
    global flash_sequence
    flash_sequence = []
    flash_colors()


def end_game():
    pass


# use tkinter await to flash the button with text color
def flash(color):
    buttons[colors.index(color)].config(bg=color)
    print(f"flashing {color} on")
    buttons[colors.index(color)].after(
        400, buttons[colors.index(color)].config(bg="white")
    )
    print(f"flashing {color} off")


# flash a random color level times
def flash_colors():
    for i in range(level):
        color = random.choice(colors)
        flash_sequence.append(color)
        print(flash_sequence)
        flash(color)


# check if the button pressed is the correct color
def button_click(color):
    global seq_pos
    global flash_sequence
    global level
    if color == flash_sequence[seq_pos]:
        print("correct")
        seq_pos += 1
    else:
        print("wrong")
        seq_pos = 0
        flash_sequence = []
        end_game()
    if seq_pos == level:
        print("next level")
        flash_sequence = []
        level += 1
        seq_pos = 0
        flash_colors()


# color button
buttons = []
for color in colors:
    buttons.append(
        Button(
            root,
            bg="white",
            height=150,
            width=150,
            text=color,
            command=partial(button_click, color),
        )
    )

# place buttons in grid
for i in range(len(buttons)):
    buttons[i].grid(row=i // 2, column=i % 2)

# start game button and init score label
start_button = Button(root, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=2)

score_label = Label(root, text="Level: 1")
score_label.grid(row=3, column=0, columnspan=2)


root.mainloop()
