from tkinter import ttk, Tk, Label, Frame, Button, Entry, StringVar, IntVar, Message, Radio
from sqlite3 import *
from random import randint
from os import path

# init local variables
local_voter_id = 0

# init database
conn = connect("voting_booth.db")
cursor = conn.cursor()

# if the database does not exist, create the schema
if path.isfile("voting_booth.db") is False:
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
    textvar=info_text,
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
first_name_label.place(relx=0.25, rely=0.25, anchor="center")
first_name_entry = Entry(registration_frame, textvariable=first_name)
first_name_entry.place(relx=0.55, rely=0.25, anchor="center")

last_name_label = Label(registration_frame, text="Last Name:")
last_name_label.place(relx=0.25, rely=0.35, anchor="center")
last_name_entry = Entry(registration_frame, textvariable=last_name)
last_name_entry.place(relx=0.55, rely=0.35, anchor="center")

# party affiliation
party_affiliation = IntVar()
parties = ["Party A", "Party B"]
party_radios = [Radio(registration_frame, text=party, variable=party_affiliation, value=i) for i, party in enumerate(parties)]
[party.place()for party in party_radios:
    

# submission (voter id generation)
def register_voter():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    report_info(f"Registering {first_name} {last_name}...")

    # generate a random 5 digit voter id that isn't already taken
    taken_voter_ids = cursor.execute("SELECT voter_id FROM voters").fetchall()
    while voter_id := randint(10000, 99999) in taken_voter_ids:
        voter_id = randint(10000, 99999)

    # add voter to database
    cursor.execute(
        "INSERT INTO voters VALUES (?, ?, ?)", (first_name, last_name, voter_id)
    )
    conn.commit()

    # display voter id


submit = Button(registration_frame, text="Submit", command=lambda: register_voter())
submit.place(relx=0.5, rely=0.45, anchor="center")

# ---------- voting ----------
voting_frame = Frame(tabs)
tabs.add(voting_frame, text="Voting")

title = Label(voting_frame, text="Voting")
title.pack()


# ---------- results ----------
results_frame = Frame(tabs)
tabs.add(results_frame, text="Results")

title = Label(results_frame, text="Results")
title.pack()


root.mainloop()
