from tkinter import *
from tkmacosx import Button
from sqlite3 import *

root = Tk()
root.geometry("500x500")


def registration():
    pass


def voting():
    pass


def results():
    pass


tabs = Frame(root, bg="black")
tabs.pack(side=BOTTOM)


def switch_tab(tab):
    tab_index = MASTER_TABS.index(tab)
    print(tab_index)
    tabs[tab_index].config(bg="white", fg="black")
    [
        inactive_tab.config(bg="grey", fg="black")
        for inactive_tab in tabs
        if inactive_tab != tabs[tab_index]
    ]


MASTER_TABS = ["Registration", "Voting", "Results"]
tabs = [
    Button(
        tabs, text=tab, bg="grey", fg="black", command=lambda tab=tab: switch_tab(tab)
    )
    for tab in MASTER_TABS
]
for col, tab in enumerate(tabs):
    tab.grid(row=0, column=col)

root.mainloop()
