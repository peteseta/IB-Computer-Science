from sqlite3 import *
from tkinter import Tk, Canvas, Entry, Frame, ttk, DISABLED, Text, StringVar

from tkmacosx import Button

# --------- database setup ---------
local_voter_id = 0
parties = ["Party A", "Party B"]

# init database
conn = connect("voting_booth.db")
cursor = conn.cursor()

# create table if it doesn't exist
if (
        len(cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
        == 0
):
    print("Creating tables...")
    cursor.execute(
        """CREATE TABLE voters(
        first_name TEXT,
        last_name TEXT,
        party_affiliation INTEGER,
        voter_id INTEGER
        )"""
    )
    conn.commit()

# --------- tkinter setup ----------

root = Tk()

notebook = ttk.Notebook(
    root,
)
notebook.grid(row=1)

root.geometry("550x750")
root.configure(bg="#1B1B1B")
root.resizable(False, False)

# ----------- title ---------------
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

# ----------- registration ---------------

first_name_entry = StringVar()
last_name_entry = StringVar()
party_affiliation_var = StringVar()


def register_voter():
    # TODO: validate input/check for complete form entry

    voter_first_name = first_name_entry.get()
    voter_last_name = last_name_entry.get()
    party_affiliation = party_affiliation_var.get()
    print(
        "registering",
        voter_first_name,
        voter_last_name,
        "with party:",
        party_affiliation,
    )

    report_info(f"Registering {voter_first_name} {voter_last_name}...")

    # generate a random 5 digit voter id that isn't already taken
    taken_voter_ids = cursor.execute("SELECT voter_id FROM voters").fetchall()
    voter_id = randint(10000, 99999)
    while voter_id in taken_voter_ids:
        voter_id = randint(10000, 99999)

    # TODO: sanitize inputs

    # add voter to database
    cursor.execute(
        "INSERT INTO voters VALUES (?, ?, ?, ?)",
        (voter_first_name, voter_last_name, party_affiliation, voter_id),
    )
    conn.commit()

    # display voter id
    report_info(f"Your voter id is {voter_id}. Please remember this number for voting.")
    print("voter id:", voter_id)


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
reg_first_name_entry = Entry(
    registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    font="Helvetica 16",
    highlightthickness=0,
)
reg_first_name_entry.place(x=30.0, y=133.0, width=430.0, height=29.0)

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
reg_last_name_entry = Entry(
    registration,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    font="Helvetica 16",
    highlightthickness=0,
)
reg_last_name_entry.place(x=30.0, y=214.0, width=430.0, height=29.0)

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
reg_dem_affil_button = Button(
    registration,
    text="Democrat",
    font="Helvetica 18",
    bg="#D4E5FF",
    fg="#000716",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("democrat clicked"),
    relief="flat",
)
reg_dem_affil_button.place(x=30.0, y=295.0, width=108.0, height=37.0)

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
reg_rep_affil_button = Button(
    registration,
    text="Republican",
    font="Helvetica 18",
    bg="#FFCDCD",
    fg="#000716",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("republican clicked"),
    relief="flat",
)
reg_rep_affil_button.place(x=145.0, y=295.0, width=118.0, height=37.0)

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
reg_submit_button = Button(
    registration,
    text="SUBMIT",
    font="Helvetica 20 bold",
    bg="black",
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("submit clicked"),
    relief="flat",
)
reg_submit_button.place(x=30.0, y=553.0, width=90.0, height=29.0)

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

# ----------- voting ---------------

voting = Frame(root)
notebook.add(voting, text="Voting")

voting_canvas = Canvas(
    voting,
    bg="#FFFFFF",
    height=617,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
voting_canvas.pack(expand=True, fill="both")

# voting id entry
voting_canvas.create_text(
    30.0,
    25.0,
    anchor="nw",
    text="enter your voter ID:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20)
)

vot_voterid_entry = Entry(
    voting,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    font=("Helvetica Bold", 36),
    highlightthickness=0
)
vot_voterid_entry.place(
    x=30.0,
    y=54.0,
    width=135.0,
    height=42.0
)

# ----- vote selector
voting_canvas.create_rectangle(
    30.0,
    198.0,
    35.0,
    324.0,
    fill="#F5F5F5",
    outline="")

voting_canvas.create_text(
    30.0,
    126.0,
    anchor="nw",
    text="SWITCH RACE",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15)
)

vot_left_arrow = Button(
    voting,
    text="←",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("left arrow clicked"),
    relief="flat"
)
vot_left_arrow.place(
    x=30.0,
    y=149.0,
    width=36.0,
    height=30.0
)

vot_right_arrow = Button(
    voting,
    text="→",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("right arrow clicked"),
    relief="flat"
)
vot_right_arrow.place(
    x=73.0,
    y=149.0,
    width=36.0,
    height=30.0
)

voting_canvas.create_text(
    118.0,
    152.0,
    anchor="nw",
    text="1 of 4",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1)
)

voting_canvas.create_text(
    44.0,
    211.0,
    anchor="nw",
    text="President",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1)
)

voting_canvas.create_text(
    44.0,
    192.0,
    anchor="nw",
    text="POSITION",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1)
)

# ----- candidate A
vot_candidate_a_button = Button(
    voting,
    bg="#F5F5F5",
    fg="#1C1C1C",
    font="Helvetica 20",
    text="Samath Gurung",
    justify="left",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("choice a clicked"),
    relief="flat",
)
vot_candidate_a_button.place(
    x=44.0,
    y=243.0,
    width=337.0,
    height=37.0
)

voting_canvas.create_text(
    293.0,
    250.0,
    anchor="nw",
    text="SELECTED",
    fill="#848484",
    font=("Helvetica Regular", 15 * -1)
)

voting_canvas.create_text(
    392.0,
    249.0,
    anchor="nw",
    text="(R)",
    fill="#C8C8C8",
    font=("Helvetica Medium", 20 * -1)
)

# ----- candidate B
candidate_b_name = StringVar(voting, "Yoyo Feng")
vot_candidate_b_button = Button(
    voting,
    bg="#F5F5F5",
    fg="#1C1C1C",
    font="Helvetica 20",
    textvariable=candidate_b_name,
    justify="left",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("choice b clicked"),
    relief="flat"
)
vot_candidate_b_button.place(
    x=44.0,
    y=287.0,
    width=337.0,
    height=37.0
)

voting_canvas.create_text(
    293.0,
    293.0,
    anchor="nw",
    text="SELECTED",
    fill="#848484",
    font=("Helvetica Regular", 15 * -1)
)

voting_canvas.create_text(
    392.0,
    293.0,
    anchor="nw",
    text="(D)",
    fill="#C8C8C8",
    font=("Helvetica Medium", 20 * -1)
)

# summary of what the user voted for
voting_canvas.create_text(
    30.0,
    370.0,
    anchor="nw",
    text="here’s who you voted for:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1)
)

vot_feedback_box = Text(
    voting,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
vot_feedback_box.place(
    x=30.0,
    y=402.0,
    width=417.0,
    height=99.0
)

# submit button
voting_canvas.create_text(
    30.0,
    525.0,
    anchor="nw",
    text="confirm your votes:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1)
)

vot_submit_button = Button(
    voting,
    text="SUBMIT",
    font="Helvetica 20 bold",
    bg="black",
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("submit clicked"),
    relief="flat"
)
vot_submit_button.place(
    x=30.0,
    y=553.0,
    width=90.0,
    height=29.0
)

# ----------- results ---------------

results = Frame(root)
notebook.add(results, text="Results")

results_canvas = Canvas(
    results,
    bg="#FFFFFF",
    height=617,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
results_canvas.pack(expand=True, fill="both")

results_canvas.create_text(
    231.0,
    44.0,
    anchor="nw",
    text="President",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1)
)

results_canvas.create_text(
    231.0,
    25.0,
    anchor="nw",
    text="RESULTS FOR",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1)
)

results_canvas.create_text(
    34.0,
    20.0,
    anchor="nw",
    text="SWITCH RACE",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1)
)

results_canvas.create_text(
    122.0,
    46.0,
    anchor="nw",
    text="1 of 4",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1)
)

res_left_arrow = Button(
    results,
    text="←",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("left arrow clicked"),
    relief="flat"
)
res_left_arrow.place(
    x=34.0,
    y=43.0,
    width=36.0,
    height=30.0
)

res_right_arrow = Button(
    results,
    text="→",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("right arrow clicked"),
    relief="flat"
)
res_right_arrow.place(
    x=77.0,
    y=43.0,
    width=36.0,
    height=30.0
)

# ----------- keep at end ------------
root.mainloop()
