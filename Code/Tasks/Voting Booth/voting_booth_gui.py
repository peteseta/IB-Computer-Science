from random import randint
from sqlite3 import *
from tkinter import Tk, Canvas, Entry, Frame, ttk, NORMAL, DISABLED, Text, StringVar, END

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkmacosx import Button

# TODO: class-ify and refactor into files

# --------- voting config ---------
# TODO: move this to a config file/database.
parties = ["'A' Party", "'B' Party"]
races = [["President", "Mr. Erik Wilensky", "Mr. Asit Meswani"],
         ["Vice President", "Ben Wong-Fodor", "Pera Kasemsripitak"],
         ["Representative", "Kun Kitilimtrakul", "Winnie Savedvanich"]]

# --------- database setup ---------
conn = connect("voting_booth.db")
conn.row_factory = lambda cursor, row: row[0]  # to make fetching a column return a simple list rather than a tuple
cursor = conn.cursor()

# create table if it doesn't exist
if (
        len(cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
        == 0
):
    print("Creating tables...")
    cursor.execute(  # table voters: for storing voter info
        """CREATE TABLE voters(
        first_name TEXT,
        last_name TEXT,
        party_affiliation INTEGER,
        voter_id INTEGER
        )"""
    )
    cursor.execute(  # table votes: for storing each vote cast for the specific race, candidate, and by the voter id
        """create table votes(
        race           TEXT    not null,
        candidate_name TEXT    not null,
        voter_id       integer not null
            constraint voter_id
                references voters (voter_id)
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
    text="voting machine #00000",
    fill="#FFFFFF",
    font=("Helvetica Bold", 32 * -1),
)

# ----------- registration ---------------

reg_first_name = StringVar()
reg_last_name = StringVar()
reg_party_affiliation = -1

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
    textvariable=reg_first_name,
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
    textvariable=reg_last_name,
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


# --- party affil buttons ---
def register_party_affil(party):
    global reg_party_affiliation
    if party == parties[0]:
        # make "selected" text element active
        registration_canvas.itemconfig(reg_rep_selected, state=DISABLED)
        registration_canvas.itemconfig(reg_a_selected, state=NORMAL)
        reg_party_affiliation = 0
    else:
        # make "selected" text element active
        registration_canvas.itemconfig(reg_a_selected, state=DISABLED)
        registration_canvas.itemconfig(reg_rep_selected, state=NORMAL)
        reg_party_affiliation = 1


# democrat party affil button
reg_a_affil_button = Button(
    registration,
    text=parties[0],
    font="Helvetica 18",
    bg="#D4E5FF",
    fg="#000716",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: register_party_affil(parties[0]),
    relief="flat",
)
reg_a_affil_button.place(x=30.0, y=295.0, width=108.0, height=37.0)

# party a selected indicator
reg_a_selected = registration_canvas.create_text(
    44.0,
    336.0,
    state=DISABLED,
    anchor="nw",
    text="SELECTED",
    fill="#C8C8C8",
    disabledfill="#FFFFFF",
    font=("Helvetica Regular", 15 * -1),
)

# party b affil button
reg_rep_affil_button = Button(
    registration,
    text=parties[1],
    font="Helvetica 18",
    bg="#FFCDCD",
    fg="#000716",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: register_party_affil(parties[1]),
    relief="flat",
)
reg_rep_affil_button.place(x=145.0, y=295.0, width=118.0, height=37.0)

# republican party selected indicator
reg_rep_selected = registration_canvas.create_text(
    165.0,
    336.0,
    state=DISABLED,
    anchor="nw",
    text="SELECTED",
    fill="#C8C8C8",
    disabledfill="#FFFFFF",
    font=("Helvetica Regular", 15 * -1),
)


# --- submission ---
def register_voter():
    # copy voter info to local variables
    voter_first_name = reg_first_name.get()
    voter_last_name = reg_last_name.get()
    voter_party_affiliation = reg_party_affiliation

    # validate input/check for complete form entry
    if voter_first_name == "" or voter_last_name == "" or voter_party_affiliation == -1:
        registration_canvas.itemconfig(reg_submit_header, text="complete all the forms.", fill="#FF0000")
        return

    registration_canvas.itemconfig(reg_submit_header, text="registration complete.", fill="#1B1B1B")
    print(f"Registering {voter_first_name} {voter_last_name} with party {voter_party_affiliation}...")

    # generate a random 5 digit voter id that isn't already taken
    taken_voter_ids = cursor.execute("SELECT voter_id FROM voters").fetchall()
    voter_id = randint(10000, 99999)
    while voter_id in taken_voter_ids:
        voter_id = randint(10000, 99999)
    print(f"Generated voter id {voter_id}.")

    # TODO: sanitize inputs / sql injection safety

    # add voter to database
    cursor.execute(
        "INSERT INTO voters VALUES (?, ?, ?, ?)",
        (voter_first_name, voter_last_name, voter_party_affiliation, voter_id),
    )
    conn.commit()

    # display voter id
    registration_canvas.itemconfig(reg_voter_id_text, text=voter_id, state=NORMAL)
    registration_canvas.itemconfig(reg_voter_id_underline, state=NORMAL)


# submit heading
reg_submit_header = registration_canvas.create_text(
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
    command=lambda: register_voter(),
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
reg_voter_id_underline = registration_canvas.create_rectangle(
    355.0, 583.0, 455.0, 589.0, fill="#F5F5F5", disabledfill="#FFFFFF", outline="", state=DISABLED
)

# voter id number
reg_voter_id_text = registration_canvas.create_text(
    455.0,
    570.0,
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
    relief="ridge",
)
voting_canvas.pack(expand=True, fill="both")

# voter id entry heading
voting_canvas.create_text(
    30.0,
    25.0,
    anchor="nw",
    text="enter your voter ID:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20),
)

# voter id entry
vot_voterid_entry = Entry(
    voting,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    font=("Helvetica Bold", 36),
    highlightthickness=0,
)
vot_voterid_entry.place(x=30.0, y=54.0, width=135.0, height=42.0)

# vertical rectangle divider for the voting pane
voting_canvas.create_rectangle(30.0, 198.0, 35.0, 324.0, fill="#F5F5F5", outline="")

# init variable for the current race the user is voting for
curr_race = 0
# all races are initialized as "not yet selected"
selections = ["not yet selected"] * 3

# text box to report the user's choices
voting_canvas.create_text(
    30.0,
    370.0,
    anchor="nw",
    text="here’s who you voted for:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)
vot_feedback_box = Text(voting, bd=0, bg="#F5F5F5", fg="#000716", highlightthickness=0, state=NORMAL, padx=5, pady=5)
vot_feedback_box.place(x=30.0, y=402.0, width=417.0, height=99.0)


# handles updating the feedback box with the user's selections each time a new selection is made
def update_feedback_box():
    vot_feedback_box.delete("1.0", END)
    vot_feedback_box.insert(END, "VOTING REPORT:\n\n")
    for count, race in enumerate(races):
        vot_feedback_box.insert(END, f"{race[0]}: {selections[count]}" + '\n')


# first time update to show the user that they have not made any selections
update_feedback_box()

# --- race details ---
voting_canvas.create_text(
    44.0,
    192.0,
    anchor="nw",
    text="POSITION",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1),
)

vot_position_name = voting_canvas.create_text(
    44.0,
    211.0,
    anchor="nw",
    text=races[curr_race][0],
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)


# handles selecting a candidate. updates the selections list and updates the feedback box.
def select_candidate(candidate):
    selections[curr_race] = candidate
    update_feedback_box()


# candidate A button + party abbreviation
vot_candidate_a_button = Button(
    voting,
    bg="#F5F5F5",
    fg="#1C1C1C",
    font="Helvetica 20",
    text=f"{races[curr_race][1]}",
    anchor="w",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_candidate(races[curr_race][1]),
    relief="flat",
    padx=0,
    pady=3,
)
vot_candidate_a_button.place(x=44.0, y=243.0, width=337.0, height=37.0)

voting_canvas.create_text(
    392.0,
    249.0,
    anchor="nw",
    text=f"({parties[0][1]})",
    fill="#C8C8C8",
    font=("Helvetica Medium", 20 * -1),
)

# candidate B button + party abbreviation
vot_candidate_b_button = Button(
    voting,
    bg="#F5F5F5",
    fg="#1C1C1C",
    font="Helvetica 20",
    anchor="w",
    text=f"{races[curr_race][2]}",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_candidate(races[curr_race][2]),
    relief="flat",
    padx=0,
    pady=3,
)
vot_candidate_b_button.place(x=44.0, y=287.0, width=337.0, height=37.0)

voting_canvas.create_text(
    392.0,
    293.0,
    anchor="nw",
    text=f"({parties[1][1]})",
    fill="#C8C8C8",
    font=("Helvetica Medium", 20 * -1),
)


# --- navigation between races ---
def select_race(direction):
    global curr_race

    # if curr is the last element, if direction is 1 then go to the first element
    if curr_race == len(races) - 1 and direction == 1:
        curr_race = 0
    # if curr_race is 0, if direction is -1 then go the last element in races
    elif curr_race == 0 and direction == -1:
        curr_race = len(races) - 1
    # if curr is not the first/last element, if direction is 1 then go to the next element
    # if curr is not the first/last element, if direction is -1 then go to the previous element
    else:
        curr_race = curr_race + direction

    # update text for the position/candidates
    voting_canvas.itemconfig(vot_nav, text=f"{curr_race + 1} of {len(races)}")
    voting_canvas.itemconfig(vot_position_name, text=races[curr_race][0])
    vot_candidate_a_button.configure(text=races[curr_race][1], anchor="center")
    vot_candidate_b_button.configure(text=races[curr_race][2], anchor="center")


voting_canvas.create_text(
    30.0,
    126.0,
    anchor="nw",
    text="SWITCH RACE",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15),
)

vot_left_arrow = Button(
    voting,
    text="←",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_race(-1),
    relief="flat",
)
vot_left_arrow.place(x=30.0, y=149.0, width=36.0, height=30.0)

vot_right_arrow = Button(
    voting,
    text="→",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_race(1),
    relief="flat",
)
vot_right_arrow.place(x=73.0, y=149.0, width=36.0, height=30.0)

vot_nav = voting_canvas.create_text(
    118.0,
    152.0,
    anchor="nw",
    text=f"{curr_race + 1} of {len(races)}",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1),
)


# --- vote submission ---
def submit_votes():
    vot_voter_id = vot_voterid_entry.get()

    # guard clause: check that all positions have a selection
    if "not yet selected" in selections:
        voting_canvas.itemconfig(vot_submit_header, text="complete your votes.", fill="#FF0000")
        return

    # guard clause: check that a voter id has been entered and that it is valid (voter id exists in voters table)
    valid_voter_ids = cursor.execute("SELECT voter_id FROM voters").fetchall()
    if len(vot_voter_id) != 5 or not vot_voter_id.isnumeric() or int(vot_voter_id) not in valid_voter_ids:
        voting_canvas.itemconfig(vot_submit_header, text="enter a valid voter id.", fill="#FF0000")
        return

    # guard clause: check for duplicate vote
    if cursor.execute("SELECT * FROM votes WHERE voter_id = ?", (vot_voter_id,)).fetchone():
        voting_canvas.itemconfig(vot_submit_header, text="already voted!", fill="#FF0000")
        return

    # for each position, add the race, candidate_name, and voter id to the votes table
    voting_canvas.itemconfig(vot_submit_header, text="voting complete.", fill="#1B1B1B")
    for i in range(len(races)):
        cursor.execute(
            "INSERT INTO votes VALUES (?, ?, ?)",
            (races[i][0], selections[i], int(vot_voter_id)),
        )
    conn.commit()


vot_submit_header = voting_canvas.create_text(
    30.0,
    525.0,
    anchor="nw",
    text="confirm your votes:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

vot_submit_button = Button(
    voting,
    text="SUBMIT",
    font="Helvetica 20 bold",
    bg="black",
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit_votes(),
    relief="flat",
)
vot_submit_button.place(x=30.0, y=553.0, width=90.0, height=29.0)

# ----------- results ---------------

results = Frame(root)
notebook.add(results, text="Results")

results_canvas = Canvas(
    results,
    bg="#FFFFFF",
    height=100,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
results_canvas.grid(row=0, column=0)

# init current race viewed by the user.
# will be incremented to 1 once the first-time rendering of the graph for the default race
# (race 1 - president) is done by calling select_graph()
curr_graph = -1


# --- navigation between races ---
def select_graph(direction):
    # displays pie chart for votes (sizes) for each candidate (labels)
    def pie(labels, sizes):
        pie_frame = Frame(results, background="#FF0000")
        pie_frame.grid(row=1, column=0)

        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)

        ax.pie(sizes, radius=0.5, labels=labels, autopct='%.1f%%',
               colors=["#D4E5FE", "#FFCDCE"],
               wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
               textprops={'size': 'large', 'color': '#1B1B1B'},
               startangle=90)

        fig.tight_layout()
        chart = FigureCanvasTkAgg(fig, pie_frame)
        chart.get_tk_widget().pack()

    global curr_graph

    # if curr is the last element, if direction is 1 then go to the first element
    if curr_graph == len(races) - 1 and direction == 1:
        curr_graph = 0
    # if curr_graph is 0, if direction is -1 then go the last element in races
    elif curr_graph == 0 and direction == -1:
        curr_graph = len(races) - 1
    # if curr is not the first/last element, if direction is 1 then go to the next element
    # if curr is not the first/last element, if direction is -1 then go to the previous element
    else:
        curr_graph = curr_graph + direction

    # update the position name and number
    results_canvas.itemconfig(res_position_name, text=f"{races[curr_graph][0]}")
    results_canvas.itemconfig(res_nav, text=f"{curr_graph + 1} of {len(races)}")

    # draw new pie chart
    candidates = [races[curr_graph][1 + i] for i in range(len(races[curr_graph]) - 1)]
    votes = [cursor.execute(
        "SELECT COUNT(*) FROM votes WHERE candidate_name = (?) and race = (?)",
        (candidates[i], races[curr_graph][0])
    ).fetchone() for i in range(len(candidates))]

    # guard clause: if no votes at all, don't draw pie
    if sum(votes) == 0:
        results_canvas.itemconfig(res_position_name, text="No votes yet!")
        return

    pie(candidates, votes)


# name of position/race results are displayed for
results_canvas.create_text(
    231.0,
    25.0,
    anchor="nw",
    text="RESULTS FOR",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1),
)
res_position_name = results_canvas.create_text(
    231.0,
    44.0,
    anchor="nw",
    text="President",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

results_canvas.create_text(
    34.0,
    20.0,
    anchor="nw",
    text="SWITCH RACE",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1),
)

res_nav = results_canvas.create_text(
    122.0,
    46.0,
    anchor="nw",
    text=f"{curr_graph + 1} of {len(races)}",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1),
)

res_left_arrow = Button(
    results,
    text="←",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_graph(-1),
    relief="flat",
)
res_left_arrow.place(x=34.0, y=43.0, width=36.0, height=30.0)

res_right_arrow = Button(
    results,
    text="→",
    fg="#C9C9C9",
    bg="#F5F5F5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_graph(1),
    relief="flat",
)
res_right_arrow.place(x=77.0, y=43.0, width=36.0, height=30.0)


# draw the pie chart for the default (first race) when its tab is selected
def on_tab_change(event):
    tab = event.widget.tab('current')['text']
    if tab == 'Results':
        select_graph(1)


notebook.bind('<<NotebookTabChanged>>', on_tab_change)

# tkinter loop
root.mainloop()
