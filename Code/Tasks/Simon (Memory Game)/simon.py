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

# master colors
colors = ["red", "green", "blue", "yellow"]

# level = how many colors are flashed
level = 1
level_text = StringVar(root, f"Level: {level}")

# instruction text
instruction_text = StringVar(root, "press start game to start")

# time of each flash
# TODO: make configurable by user
speed = 300

# master sequence of colors and position in sequence to check ti
seq_pos = 0
flash_sequence = []

# clear sequence and flash
def start_game():
    global level
    global flash_sequence
    global seq_pos

    flash_sequence = []
    seq_pos = 0
    level = 1
    level_text.set(f"Level: {level}")
    instruction_text.set("watch.")
    simon_sequence()


def start_new_level():
    global level
    global flash_sequence
    global seq_pos

    flash_sequence = []
    seq_pos = 0
    level += 1
    level_text.set(f"Level: {level}")
    instruction_text.set("watch.")
    simon_sequence()


# TODO: store highscore and quit
def end_game():
    disable_buttons()
    instruction_text.set("game over. press start game to play again.")


# make buttons clickable
def enable_buttons():
    for button in buttons:
        button.config(state=NORMAL)


# make buttons unclickable while flashing or when game is over
def disable_buttons():
    for button in buttons:
        button.config(state=DISABLED)


# flash the button "color" the color "color"
def flash_on(color, speed):
    root.after(speed, buttons[colors.index(color)].config(bg=color))
    print(f"flashing {color} on")


# reset button "color" back to white
def flash_off(color, speed):
    root.after(speed, buttons[colors.index(color)].config(bg="white"))
    root.update()
    print(f"flashing {color} off")


# flash a random color "level" times
def simon_sequence():
    disable_buttons()
    for i in range(level):
        color = random.choice(colors)
        flash_sequence.append(color)
        print(flash_sequence)
        flash_on(color, speed)
        root.update()
        flash_off(color, speed)
    instruction_text.set("now your turn.")
    enable_buttons()


# check if the button pressed is the correct color
def button_click(color):
    global seq_pos
    global flash_sequence
    global level

    if seq_pos == level - 1:
        print("next level")
        instruction_text.set("watch.")
        start_new_level()
    elif color == flash_sequence[seq_pos]:
        print("correct")
        seq_pos += 1
    else:
        print("wrong")
        end_game()


# add a button for each color in the colors list
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

# place buttons in grid. adapts to number of colors
for i in range(len(buttons)):
    buttons[i].grid(row=i // 2, column=i % 2)

# start game button and init score label
start_button = Button(root, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=2)

score_label = Label(root, textvar=level_text)
score_label.grid(row=3, column=0, columnspan=2)

instruction_label = Label(root, textvar=instruction_text)
instruction_label.grid(row=4, column=0, columnspan=2)


root.mainloop()
