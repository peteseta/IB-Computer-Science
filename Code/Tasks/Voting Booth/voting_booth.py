from os import path
from random import randint
from sqlite3 import *
from tkinter import (
    ttk,
    Tk,
    Label,
    Frame,
    Button,
    Entry,
    StringVar,
    Message,
    Radiobutton,
)

# setup (for now)
# improvement: make this OOP
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

# init gui
root = Tk()
root.title("Voting Booth v0.1")
root.geometry("500x500")

# tab setup
tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True)

# info pane setup
info = Frame(root)
info.pack(fill="both", pady=10)

info_text = StringVar()
msg = Message(
    info,
    textvariable=info_text,
    width=400,
)
msg.pack()


def report_info(text):
    info_text.set(info_text.get() + "\n" + text)


# ---------- registration ----------
registration_frame = Frame(tabs)
tabs.add(registration_frame, text="Voter Registration")

title = Label(registration_frame, text="Registration", font="system 20 bold")
title.place(relx=0.5, rely=0.10, anchor="center")
subtitle = Label(
    registration_frame, text="Please enter your information below to register to vote."
)
subtitle.place(relx=0.5, rely=0.16, anchor="center")

# name entry
first_name = StringVar()
last_name = StringVar()

first_name_label = Label(registration_frame, text="First Name:")
first_name_label.place(relx=0.32, rely=0.25, anchor="e")
first_name_entry = Entry(registration_frame, textvariable=first_name)
first_name_entry.place(relx=0.55, rely=0.25, anchor="center")

last_name_label = Label(registration_frame, text="Last Name:")
last_name_label.place(relx=0.32, rely=0.35, anchor="e")
last_name_entry = Entry(registration_frame, textvariable=last_name)
last_name_entry.place(relx=0.55, rely=0.35, anchor="center")

# party affiliation
party_label = Label(registration_frame, text="Party Affiliation:")
party_label.place(relx=0.25, rely=0.45)

party_affiliation_var = StringVar(registration_frame)
party_radios = [
    Radiobutton(registration_frame, text=party, variable=party_affiliation_var, value=i)
    for i, party in enumerate(parties)
]
for i, radio in enumerate(party_radios):
    radio.place(relx=0.60, rely=0.45 + (i * 0.05), anchor="n")


# submission (voter id generation)
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


submit = Button(registration_frame, text="Submit", command=lambda: register_voter())
submit.place(relx=0.5, rely=(party_radios[-1].winfo_y() + 0.65), anchor="center")

# TODO: ---------- voting ----------
voting_frame = Frame(tabs)
tabs.add(voting_frame, text="Voting")

title = Label(voting_frame, text="Voting")
title.pack()

# TODO: ---------- results ----------
results_frame = Frame(tabs)
tabs.add(results_frame, text="Results")

title = Label(results_frame, text="Results")
title.pack()

root.mainloop()
