from tkinter import Tk, Frame, Label, StringVar, NORMAL, DISABLED
from tkmacosx import Button
from random import choice
from functools import partial

# shorthand to enable or disable the clicking of buttons
disable_buttons = lambda: [b.config(state=DISABLED) for b in buttons]
enable_buttons = lambda: [b.config(state=NORMAL) for b in buttons]

# config - starting level
level = 0
# config - default time of each flash
speed = 300

# adjusts the speed of the flashing through the bottom buttons.
def adjust_speed(amt):
    global speed
    if amt == "reset":
        speed = 300
    elif speed + amt > 0 and speed + amt <= 1000:
        speed = speed + int(amt)
    speed_text.set(f"Speed: {speed}ms")


# reset level to 0 and call the flash
def start_game():
    global level
    level = 0
    simon()


# disable buttons and display game over message
def end_game():
    disable_buttons()
    instruction_text.set("Game over!")


# if the score is higher than the previous highscore, update the highscore
def highscore(level):
    # a hack here to not have to use a global variable for the highscore
    if level > int(highscore_text.get().split(" ")[1]):
        highscore_text.set(f"Highscore: {level}")
    return


def simon():
    global flash_sequence
    flash_sequence = []

    global seq_pos
    seq_pos = 0

    global level
    level += 1

    # flash the button "color" the color "color"
    def flash_on(color, speed):
        root.after(speed // 2, buttons[colors.index(color)].config(bg=color))
        print(f"flashing {color} on")

    # reset button "color" back to white
    def flash_off(color, speed):
        root.after(speed, buttons[colors.index(color)].config(bg="white"))
        root.update()
        print(f"flashing {color} off")

    instruction_text.set("Watch.")
    level_text.set(f"Level: {level}")

    disable_buttons()

    # flash a random color "level" times and append it to the sequence each time
    for i in range(level):
        color = choice(colors)
        flash_sequence.append(color)
        print(flash_sequence)
        flash_on(color, speed)
        root.update()
        flash_off(color, speed)

    instruction_text.set("Now your turn.")
    enable_buttons()


# each time a button is pressed, check if it is the correct color in the correct pos in the sequence
def button_click(color):
    global seq_pos
    global level

    # if all the colors are correct, move to a new level.
    if seq_pos == level - 1:
        print("new level")
        highscore(level)
        simon()
    elif color == flash_sequence[seq_pos]:
        print("correct")
        seq_pos += 1
    else:
        print("wrong")
        end_game()


# init the window
root = Tk()
root.title("Simon Memory Game")

# master color list
colors = ["red", "green", "blue", "yellow"]

# add a button for each color in the colors list
button_frame = Frame(root)
button_frame.pack()

buttons = []
for color in colors:
    buttons.append(
        Button(
            button_frame,
            bg="white",
            height=150,
            width=150,
            # text=color,
            command=partial(button_click, color),
        )
    )

# place buttons in grid. adapts to number of colors
for i in range(len(buttons)):
    buttons[i].grid(row=i // 2, column=i % 2)

# labels for level, score and status + new game button
info_frame = Frame(root)
info_frame.pack(pady=20)

level_text = StringVar(info_frame, "Level: 0")
highscore_text = StringVar(info_frame, "Highscore: 0")
instruction_text = StringVar(info_frame, 'Press "New Game" to play')
speed_text = StringVar(info_frame, f"Speed: {speed}ms")

# start game button and init score label
start_button = Button(info_frame, text="New Game", command=start_game)
start_button.grid(row=0, column=0)

score_label = Label(info_frame, textvar=level_text)
score_label.grid(row=0, column=2, sticky="E")

highscore_label = Label(info_frame, textvar=highscore_text)
highscore_label.grid(row=1, column=2, sticky="W")

instruction_label = Label(
    info_frame,
    textvar=instruction_text,
    font="system 14 bold",
    width=20,
)
instruction_label.grid(row=0, column=1)

# adjustment of speed of flashing
speed_adj_frame = Frame(root)
speed_adj_frame.pack()

# up down arrow to configure speed
speed_label = Label(speed_adj_frame, textvar=speed_text)
speed_label.grid(row=0, column=0, columnspan=2)

speed_up = Button(
    speed_adj_frame, text="▲", width=50, command=lambda: adjust_speed(100)
)
speed_up.grid(row=1, column=0)

speed_reset = Button(
    speed_adj_frame, text="↺", width=50, command=lambda: adjust_speed("reset")
)
speed_reset.grid(row=1, column=1)

speed_down = Button(
    speed_adj_frame, text="▼", width=50, command=lambda: adjust_speed(-100)
)
speed_down.grid(row=1, column=2)

root.mainloop()
