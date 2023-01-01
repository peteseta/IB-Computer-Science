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
# fully dynamic! add or remove races and candidates and the ui will update accordingly.
races = [["President", "Mr. Erik Wilensky", "Mr. Asit Meswani"],
         ["Vice President", "Ben Wong-Fodor", "Pera Kasemsripitak"],
         ["Representative", "Kun Kitilimtrakul", "Winnie Savedvanich"]]

# --------- database setup ---------
conn = connect("voting_booth.db")
# to make fetching a column return a list/single element rather than a 1-element-tuple for each element
conn.row_factory = lambda cursor, row: row[0]
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


# --------- helper functions ---------
# determines the index of the next race when using forward/back buttons
def next_back_navigation(curr, direction):  # direction: 1 for next, -1 for back
    # if curr is the last element, if direction is 1 then go to the first element
    if curr == len(races) - 1 and direction == 1:
        return 0
    # if curr_graph is 0, if direction is -1 then go the last element in races
    elif curr == 0 and direction == -1:
        return len(races) - 1
    # if curr is not the first/last element, if direction is 1 then go to the next element
    # if curr is not the first/last element, if direction is -1 then go to the previous element
    else:
        return curr + direction


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

# init registration variables
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

# --- title ---
registration_canvas.create_rectangle(0.0, 0.0, 500.0, 81.0, fill="#F5F5F5", outline="")

registration_canvas.create_text(
    30.0,
    18.0,
    anchor="nw",
    text="registration",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

registration_canvas.create_text(
    30.0,
    39.0,
    anchor="nw",
    text="enter your information to register to vote.",
    fill="#1B1B1B",
    font=("Helvetica Regular", 20 * -1),
)

# --- personal detail entry ---
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

# party affiliation heading
registration_canvas.create_text(
    30.0,
    263.0,
    anchor="nw",
    text="party affiliation",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)


# --- party affiliation ---
# sets the party affil variable and shows the "selected" text below the button of the chosen party
def register_party_affil(party):
    global reg_party_affiliation
    if party == parties[0]:
        # make "selected" text element active
        registration_canvas.itemconfig(reg_b_selected, state=DISABLED)
        registration_canvas.itemconfig(reg_a_selected, state=NORMAL)
        reg_party_affiliation = 0
    else:
        # make "selected" text element active
        registration_canvas.itemconfig(reg_a_selected, state=DISABLED)
        registration_canvas.itemconfig(reg_b_selected, state=NORMAL)
        reg_party_affiliation = 1


# party a affiliation button
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

# party b affiliation button
reg_b_affil_button = Button(
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
reg_b_affil_button.place(x=145.0, y=295.0, width=118.0, height=37.0)

# party b selected indicator
reg_b_selected = registration_canvas.create_text(
    165.0,
    336.0,
    state=DISABLED,
    anchor="nw",
    text="SELECTED",
    fill="#C8C8C8",
    disabledfill="#FFFFFF",
    font=("Helvetica Regular", 15 * -1),
)


# --- registration submission ---
def register_voter():
    # copy voter info to local variables
    voter_first_name = reg_first_name.get()
    voter_last_name = reg_last_name.get()
    voter_party_affiliation = reg_party_affiliation

    # guard clause: validate input/check for complete form entry
    if voter_first_name == "" or voter_last_name == "" or voter_party_affiliation == -1:
        registration_canvas.itemconfig(reg_submit_header, text="complete all the forms.", fill="#FF0000")
        return

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

    # display success message
    registration_canvas.itemconfig(reg_submit_header, text="registration complete.", fill="#1B1B1B")
    print(f"Registered {voter_first_name} {voter_last_name} with party {voter_party_affiliation}...")

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

# --- voter id display ---
registration_canvas.create_text(
    325.0,
    525.0,
    anchor="nw",
    text="your voter ID:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20 * -1),
)

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

selections = ["not yet selected"] * len(races)  # all races are initialized as "not yet selected"

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

# --- title and voter id entry ---
voting_canvas.create_text(
    30.0,
    25.0,
    anchor="nw",
    text="enter your voter ID:",
    fill="#1B1B1B",
    font=("Helvetica Bold", 20),
)

vot_voterid_entry = Entry(
    voting,
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    font=("Helvetica Bold", 36),
    highlightthickness=0,
)
vot_voterid_entry.place(x=30.0, y=54.0, width=135.0, height=42.0)

# --- selection feedback ---
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
    vot_feedback_box.delete("1.0", END)  # clear the feedback box
    vot_feedback_box.insert(END, "VOTING REPORT:\n\n")  # add header
    for count, race in enumerate(races):  # add each selection
        vot_feedback_box.insert(END, f"{race[0]}: {selections[count]}" + '\n')


# first time update to show the user that they have not made any selections
update_feedback_box()

# --- race selection ---

# vertical rectangle divider for the voting pane
voting_canvas.create_rectangle(30.0, 198.0, 35.0, 324.0, fill="#F5F5F5", outline="")

# init variable for the current race the user is voting for
curr_race = 0

# --- position + candidate details ---
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


# handles selecting a candidate. called each time a candidate's button is pressed
def select_candidate(candidate):
    selections[curr_race] = candidate  # update selections list
    update_feedback_box()  # update the feedback box


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


# --- navigation and ui updating logic for going next and back between races ---
def select_race(direction):
    global curr_race
    curr_race = next_back_navigation(curr_race, direction)  # get index of next race to be displayed

    # update text for the navigation, race, and candidate names
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

# navigation text (e.g. 1 of 4)
vot_nav = voting_canvas.create_text(
    118.0,
    152.0,
    anchor="nw",
    text=f"{curr_race + 1} of {len(races)}",
    fill="#C8C8C8",
    font=("Helvetica Regular", 15 * -1),
)


# --- vote submission ---
def submit_votes():  # called when the submit button is pressed
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

    # for each race, add the race name, chosen candidate name, and voter id to the votes table
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


def show_results():
    # plot a percentage proportional stacked bar chart (election poll style)
    bar_frame = Frame(results, background="#FF0000")
    bar_frame.grid(row=1, column=0)

    def draw_chart():
        # total number of votes for each position
        total_votes = [sum(x) for x in vote_results]

        # percentage of votes for each position
        candidate_1_perc = [round(x[0] / y * 100, 1) for x, y in zip(vote_results, total_votes)]
        candidate_2_perc = [round(x[1] / y * 100, 1) for x, y in zip(vote_results, total_votes)]

        fig = Figure(figsize=(5, 6.2), dpi=100)
        ax = fig.add_subplot(111)

        for i in range(len(races)):
            # horizontal bars
            ax.barh(3 - i, candidate_2_perc[i], height=0.4, label=races[i][1], left=candidate_1_perc[i])
            ax.barh(3 - i, candidate_1_perc[i], height=0.4, label=races[i][2])

            # label of race
            ax.text(0, 3 - i + 0.3, races[i][0], ha='left', va='center', fontfamily='Helvetica', fontweight='bold',
                    fontsize='large')

            # labels for left side candidate
            ax.text(2, 3 - i + 0.1, races[i][1], ha='left', va='center', fontfamily='Helvetica', fontweight='bold')
            ax.text(2, 3 - i, str(candidate_1_perc[i]) + "% of votes", ha='left', va='center',
                    fontfamily='Helvetica')
            ax.text(2, 3 - i - 0.1, str(vote_results[i][0]) + " votes", ha='left', va='center', fontfamily='Helvetica')

            # labels for right side candidate
            ax.text(98, 3 - i + 0.1, races[i][2], ha='right', va='center', fontfamily='Helvetica', fontweight='bold')
            ax.text(98, 3 - i, str(candidate_2_perc[i]) + "% of votes", ha='right', va='center', fontfamily='Helvetica')
            ax.text(98, 3 - i - 0.1, str(vote_results[i][1]) + " votes", ha='right', va='center',
                    fontfamily='Helvetica')

        # labels
        ax.set_xlabel('Percentage of Votes')
        ax.set_xticks(range(0, 101, 10))
        ax.set_yticks([])

        # no borders
        fig.tight_layout()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        chart = FigureCanvasTkAgg(fig, bar_frame)
        chart.get_tk_widget().pack()

    # fetch name and vote count data for the candidates of the current race
    vote_results = [[0] * 2 for _ in range(len(races))]
    for race in range(len(races)):
        for candidate in range(len(races[race]) - 1):
            vote_results[race][candidate] = \
                cursor.execute("SELECT COUNT(*) FROM votes WHERE candidate_name = (?) AND race = (?)",
                               (races[race][candidate + 1], races[race][0])).fetchone()

    # guard clause: if no votes at all, don't draw pie
    if 0 in map(sum, vote_results):
        print("no votes yet!")
    else:
        draw_chart()


# draw a new chart for the default race (0 - president) every time the results tab is opened
notebook.bind('<<NotebookTabChanged>>',
              lambda event: show_results() if event.widget.tab('current')['text'] == 'Results' else None)

# tkinter loop
root.mainloop()
