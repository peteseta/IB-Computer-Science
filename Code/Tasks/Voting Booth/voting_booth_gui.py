from tkinter import Tk, Canvas, Entry, Frame, ttk, DISABLED
from tkmacosx import Button

root = Tk()

notebook = ttk.Notebook(
    root,
)
notebook.grid(row=1)

root.geometry("550x750")
root.configure(bg="#1B1B1B")
root.resizable(False, False)

# just for the title
title_canvas = Canvas(
    root, bg="#1B1B1B", height=83, width=550, bd=0, highlightthickness=0, relief="flat"
)
title_canvas.grid(row=0)

# big title
title_canvas.create_text(
    30.0,
    24.0,
    anchor="nw",
    text="voting machine #53716",
    fill="#FFFFFF",
    font=("Helvetica Bold", 32 * -1),
)

registration = Frame(root)
notebook.add(registration, text="Registration")

registration_canvas = Canvas(
    registration,
    bg="#FFFFFF",
    height=610,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="flat",
)
registration_canvas.pack(expand=True, fill="both")

registration_canvas.create_rectangle(0.0, 0.0, 500.0, 81.0, fill="#F5F5F5", outline="")

# title
registration_canvas.create_text(
    30.0,
    18.0,
    anchor="nw",
    text="registration",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

# subtitle
registration_canvas.create_text(
    30.0,
    39.0,
    anchor="nw",
    text="enter your information to register to vote.",
    fill="#1B1B1B",
    font=("Helvetica Regular", 20 * -1),
)

# first name heading
registration_canvas.create_text(
    30.0,
    101.0,
    anchor="nw",
    text="first name",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

# first name entry
entry_1 = Entry(
    registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    font="Helvetica 16",
    highlightthickness=0,
)
entry_1.place(x=30.0, y=133.0, width=430.0, height=29.0)

# last name heading
registration_canvas.create_text(
    30.0,
    183.0,
    anchor="nw",
    text="last name",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

# last name entry
entry_2 = Entry(
    registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    font="Helvetica 16",
    highlightthickness=0,
)
entry_2.place(x=30.0, y=214.0, width=430.0, height=29.0)

# party affil heading
registration_canvas.create_text(
    30.0,
    263.0,
    anchor="nw",
    text="party affiliation",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

# democrat party affil button
button_2 = Button(
    registration,
    text="Democrat",
    font="Helvetica 18",
    bg="#D4E5FF",
    fg="#000716",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
)
button_2.place(x=30.0, y=295.0, width=108.0, height=37.0)

# democrat party selected indicator
registration_canvas.create_text(
    44.0,
    332.0,
    state=DISABLED,
    anchor="nw",
    text="SELECTED",
    fill="#C8C8C8",
    disabledfill="#FFFFFF",
    font=("Helvetica Regular", 15 * -1),
)

# republican party affil button
button_3 = Button(
    registration,
    text="Republican",
    font="Helvetica 18",
    bg="#FFCDCD",
    fg="#000716",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
)
button_3.place(x=145.0, y=295.0, width=118.0, height=37.0)

# republican party selected indicator
registration_canvas.create_text(
    165.0,
    332.0,
    state=DISABLED,
    anchor="nw",
    text="SELECTED",
    fill="#C8C8C8",
    disabledfill="#FFFFFF",
    font=("Helvetica Regular", 15 * -1),
)

# submit heading
registration_canvas.create_text(
    30.0,
    525.0,
    anchor="nw",
    text="submit information:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

# submit button
button_1 = Button(
    registration,
    text="SUBMIT",
    font="Helvetica 20 bold",
    bg="black",
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(x=30.0, y=553.0, width=90.0, height=29.0)

# voter id heading
registration_canvas.create_text(
    325.0,
    525.0,
    anchor="nw",
    text="your voter ID:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

# voter id highlight
registration_canvas.create_rectangle(
    355.0, 583.0, 455.0, 589.0, fill="#F5F5F5", outline=""
)

# voter id number
registration_canvas.create_text(
    455.0,
    575.0,
    state=DISABLED,
    anchor="e",
    text="00000",
    fill="#1B1B1B",
    disabledfill="#F0F0F0",
    font=("Helvetica Bold", 36 * -1),
)

window2 = Frame(root)
notebook.add(window2, text="Voting")

root.mainloop()
