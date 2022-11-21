# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    500.0,
    83.0,
    fill="#1B1B1B",
    outline="")

canvas.create_rectangle(
    0.0,
    81.0,
    500.0,
    164.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    337.0,
    656.0,
    460.0,
    666.0,
    fill="#F5F5F5",
    outline="")

canvas.create_text(
    30.0,
    24.0,
    anchor="nw",
    text="voting machine #0000",
    fill="#FFFFFF",
    font=("SFPro Bold", 32 * -1)
)

canvas.create_text(
    30.0,
    99.0,
    anchor="nw",
    text="registration",
    fill="#1B1B1B",
    font=("SFPro Bold", 20 * -1)
)

canvas.create_text(
    30.0,
    182.0,
    anchor="nw",
    text="first name",
    fill="#1B1B1B",
    font=("SFPro Bold", 20 * -1)
)

canvas.create_text(
    30.0,
    264.0,
    anchor="nw",
    text="last name",
    fill="#1B1B1B",
    font=("SFPro Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=30.0,
    y=634.0,
    width=90.0,
    height=29.0
)

canvas.create_text(
    30.0,
    344.0,
    anchor="nw",
    text="party affiliation",
    fill="#1B1B1B",
    font=("SFPro Bold", 20 * -1)
)

canvas.create_text(
    30.0,
    606.0,
    anchor="nw",
    text="submit information:",
    fill="#1B1B1B",
    font=("SFPro Bold", 20 * -1)
)

canvas.create_text(
    325.0,
    606.0,
    anchor="nw",
    text="your voter ID:",
    fill="#1B1B1B",
    font=("SFPro Bold", 20 * -1)
)

canvas.create_text(
    30.0,
    120.0,
    anchor="nw",
    text="enter your information to register to vote.",
    fill="#1B1B1B",
    font=("SFPro Regular", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    245.0,
    229.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=30.0,
    y=214.0,
    width=430.0,
    height=29.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    245.0,
    310.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=30.0,
    y=295.0,
    width=430.0,
    height=29.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=30.0,
    y=376.0,
    width=108.0,
    height=37.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=145.0,
    y=376.0,
    width=118.0,
    height=37.0
)

canvas.create_text(
    340.0,
    636.0,
    anchor="nw",
    text="00000",
    fill="#1B1B1B",
    font=("SFPro Bold", 36 * -1)
)

canvas.create_text(
    44.0,
    413.0,
    anchor="nw",
    text="SELECTED",
    fill="#C8C8C8",
    font=("SFPro Regular", 15 * -1)
)

canvas.create_text(
    165.0,
    413.0,
    anchor="nw",
    text="SELECTED",
    fill="#C8C8C8",
    font=("SFPro Regular", 15 * -1)
)
window.resizable(False, False)
window.mainloop()
