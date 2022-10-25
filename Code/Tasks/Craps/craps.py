from random import randint
from tkinter import CENTER, Button, Entry, Frame, IntVar, Label, StringVar, Tk

# unicode symbols of each dice face
dice_unicode = {
    1: "\u2680",
    2: "\u2681",
    3: "\u2682",
    4: "\u2683",
    5: "\u2684",
    6: "\u2685",
}

# init root object + window/set window size
app_title = "Crap_Craps v0.7"
root = Tk(className=app_title)
root.geometry("400x200")

# global tkinter IntVar type counts
global_wins = IntVar(root, value=0)
global_losses = IntVar(root, value=0)
global_ties = IntVar(root, value=0)
global_money = IntVar(root, value=0)
global_bet_amount = IntVar(root, value=0)

# global variable for the point (if there is a point after the come out roll)
global_round_point = 0

# shorthand for updating global variables
def update_global_count(var, count):
    var.set(count)


# add money to the global money variable - after win or lose
def payout(type):
    if type == 1:
        # 1:1 payout - get money back + money equivalent to however much was bet
        global_money.set(int(global_money.get()) + (2 * int(global_bet_amount.get())))
    if type == 0:
        # in a tie, you only get your money back
        global_money.set(int(global_money.get()) + int(global_bet_amount.get()))


# rolls two random dice, displays a frame with a graphic of the dice and the sum
def roll_dice(source):
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    dice_window = Frame(source, width=200)
    dice_window.grid(row=0, column=2)

    dice1 = Label(
        dice_window, text=dice_unicode[d1], font=("Helvetica", 50), fg="black"
    )
    dice1.grid(row=0, column=0)
    dice2 = Label(
        dice_window, text=dice_unicode[d2], font=("Helvetica", 50), fg="black"
    )
    dice2.grid(row=0, column=1)

    sum_dice = Label(dice_window, text="= " + str(d1 + d2), font=("System", 30))
    sum_dice.grid(row=0, column=2)

    return d1 + d2


# at this point, the user has won or lost the game
def end_screen_frame(global_root, source):
    source.destroy()

    # handles quitting the game
    def quit_game():
        exit()

    # handles restarting the game - only if there is money left
    def new_game():
        if int(global_money.get()) > 0:
            make_bet_frame(global_root, end_screen)
        else:
            game_over.configure(text="You have no money left!", fg="red")

    end_screen = Frame(global_root)
    end_screen.pack(anchor=CENTER)

    game_over = Label(end_screen, text="Round Over. Do you want to play again?")
    game_over.grid(row=0, column=1)

    # prompt user to play again or let them quit the game.
    play_again = Button(end_screen, text="Yes", command=lambda: new_game())
    play_again.grid(row=1, column=0)

    end_game = Button(end_screen, text="No", command=lambda: quit_game())
    end_game.grid(row=1, column=2)


def point_frame(global_root, come_out_roll, point):
    come_out_roll.destroy()

    point = Frame(global_root)
    point.pack(anchor=CENTER)

    # init variable for displaying the result of the roll
    result_text_var = StringVar()
    if bet == 1:
        # need to get point
        result_text_var.set(
            "Roll the dice. You have to roll a " + str(global_round_point) + "."
        )
    elif bet == 0:
        # need to get a 7
        result_text_var.set("Roll the dice. You have to roll a 7.")

    # calculates the result based on the rolled dice
    # 1. if win/loss: calculate payout and credit money
    # 2. update the global counts for win/loss/tie
    # 3. let the user know their result
    def calculate_point_roll(dice):
        if dice == 7:
            if bet == 0:
                # win
                payout(1)
                update_global_count(global_wins, global_wins.get() + 1)
                result_text_var.set("You win!")
                return 1
            else:
                # lose
                update_global_count(global_losses, global_losses.get() + 1)
                result_text_var.set("You lose!")
                return 0
        elif dice == global_round_point:
            if bet == 0:
                # lose
                update_global_count(global_losses, global_losses.get() + 1)
                result_text_var.set("You lose!")
                return 0
            else:
                # win
                payout(1)
                update_global_count(global_wins, global_wins.get() + 1)
                result_text_var.set("You win!")
                return 1
        elif bet == 1:
            # need to get point
            result_text_var.set("You have to roll a " + str(global_round_point) + ".")
            return 2
        elif bet == 0:
            # need to get a 7
            result_text_var.set("You have to roll a 7.")
            return 3

    # rolls the dice and calculates the result each time
    def point_roll():
        dice = roll_dice(point)
        result = calculate_point_roll(dice)

        # if there is a win or loss, destroy the roll button and prompt the user to go to end_screen
        if result == 0 or result == 1:
            point_button.destroy()
            payout(1) if result == 1 else None
            point_next = Button(
                point, text="Next", command=lambda: end_screen_frame(global_root, point)
            )
            point_next.grid(row=1, column=2)

    point_button = Button(point, text="Roll", command=lambda: point_roll())
    point_button.grid(row=3, column=2)

    # label updated with result of the roll once rolled
    point_result = Label(point, textvariable=result_text_var, font="System 15 bold")
    point_result.grid(row=2, column=2)


def come_out_roll_frame(global_root, make_bet):
    make_bet.destroy()

    come_out_roll = Frame(global_root)
    come_out_roll.pack(anchor=CENTER)

    # init variable to show the result of the roll
    result_text_var = StringVar()
    result_text_var.set("Roll the dice!")

    # check conditions for winning/losing based on bet; else there is a point
    def calculate_first_roll(dice):
        if bet == 1:
            if dice == 7 or dice == 11:
                # win
                payout(1)
                update_global_count(global_wins, global_wins.get() + 1)
                result_text_var.set("You win!")
                return 1
            elif dice == 2 or dice == 3 or dice == 12:
                # lose
                update_global_count(global_losses, global_losses.get() + 1)
                result_text_var.set("You lose!")
                return 0
            else:
                # point
                result_text_var.set("Point!")
                return 3
        elif bet == 0:
            if dice == 2 or dice == 3:
                # win
                payout(1)
                update_global_count(global_wins, global_wins.get() + 1)
                result_text_var.set("You win!")
                return 1
            elif dice == 7 or dice == 11:
                # lose
                update_global_count(global_losses, global_losses.get() + 1)
                result_text_var.set("You lose!")
                return 0
            elif dice == 12:
                # tie
                payout(0)
                update_global_count(global_ties, global_ties.get() + 1)
                result_text_var.set("Tie!")
                return 2
            else:
                # point
                result_text_var.set("Point!")
                return 3

    # rolls dice and shows result
    def first_roll():
        dice = roll_dice(come_out_roll)
        result = calculate_first_roll(dice)

        # set the global round point variable
        global global_round_point
        global_round_point = dice

        # destroy the title and button as there is only one first roll.
        come_out_roll_button.destroy()
        come_out_roll_title.destroy()

        # prompt the user to go to the next frame:
        # for a win/lose, go to the end. for a point, go to the point frame.
        come_out_roll_next = Button(
            come_out_roll,
            text="Next",
            command=lambda: point_frame(global_root, come_out_roll, dice)
            if result == 3
            else end_screen_frame(global_root, come_out_roll),
        )
        come_out_roll_next.grid(row=4, column=2)

    come_out_roll_title = Label(come_out_roll, text="Time for the come out roll!")
    come_out_roll_title.grid(row=0, column=2)

    come_out_roll_button = Button(
        come_out_roll, text="Roll", command=lambda: first_roll()
    )
    come_out_roll_button.grid(row=1, column=2)

    come_out_roll_label = Label(come_out_roll, textvariable=result_text_var)
    come_out_roll_label.grid(row=2, column=2)


# make_bet helper function - deduct the amount betted from money
def set_global_bet():
    global_money.set(int(global_money.get()) - int(global_bet_amount.get()))


def make_bet_frame(global_root, source, is_title=0):
    # draw the info frame only on the first time
    info_frame(global_root) if is_title else None
    source.destroy()

    # init variable for the value of the bet
    bet_amount = StringVar()

    # when the bet_amount entrybox updates, update global variable bet_amount
    bet_amount.trace(
        "w",
        lambda name, index, mode, sv=bet_amount: update_global_count(
            global_bet_amount, bet_amount.get()
        ),
    )

    # shows an error message if number is invalid
    def bet_amount_error():
        make_bet_amount_label.configure(text="Please enter a valid number!", fg="red")

    # goes to the come out roll frame if the bet amount is valid
    def pass_line(global_root, make_bet):
        global bet
        bet = 1
        if (
            bet_amount.get().isdigit()
            and int(bet_amount.get()) <= int(global_money.get())
            and int(bet_amount.get()) != 0
        ):
            set_global_bet()
            come_out_roll_frame(global_root, make_bet)
        else:
            bet_amount_error()

    def no_pass_line(global_root, make_bet):
        global bet
        bet = 0
        if (
            bet_amount.get().isdigit()
            and int(bet_amount.get()) <= int(global_money.get())
            and int(bet_amount.get()) != 0
        ):
            set_global_bet()
            come_out_roll_frame(global_root, make_bet)
        else:
            bet_amount_error()

    make_bet = Frame(global_root)
    make_bet.pack(anchor=CENTER)

    make_bet_label = Label(make_bet, text="Make your bet!", font="System 15 bold")
    make_bet_label.grid(row=0, column=1)

    make_bet_amount_label = Label(make_bet, text="Bet amount:")
    make_bet_amount_label.grid(row=1, column=1)

    make_bet_amount = Entry(make_bet, textvariable=bet_amount)
    make_bet_amount.grid(row=2, column=1)

    make_bet_button_pass = Button(
        make_bet, text="Pass Line", command=lambda: pass_line(global_root, make_bet)
    )
    make_bet_button_pass.grid(row=3, column=0)

    make_bet_button_nopass = Button(
        make_bet,
        text="No Pass Line",
        command=lambda: no_pass_line(global_root, make_bet),
    )
    make_bet_button_nopass.grid(row=3, column=2)


def title_frame(global_root):

    # variable for amount of starting money
    starting_money = StringVar()

    # when starting_money is updated, call update_global_variable(starting_money) to update the global money
    starting_money.trace(
        "w",
        lambda name, index, mode, sv=starting_money: update_global_count(
            global_money, starting_money.get()
        ),
    )

    title = Frame(global_root)
    title.pack(anchor=CENTER)

    title_label = Label(
        title,
        text="Welcome to Crap Craps!",
        font="System 15 bold",
    )
    title_label.pack()

    play_label = Label(title, text="To start, press Play.", font="System 15")
    play_label.pack()

    payout_desc = Label(
        title,
        text="A pass line bet pays 1:1, a no pass line bet pays 1:1. If you tie, you get your money back. If you lose, you lose your bet!",
        wraplength=370,
    )
    payout_desc.pack()

    chip_exchange_label = Label(
        title, text="Enter the amount of money you want to exchange."
    )
    chip_exchange_label.pack()
    chip_exchange = Entry(title, textvariable=starting_money)
    chip_exchange.pack()

    title_button = Button(
        title,
        text="Play",
        command=lambda: make_bet_frame(global_root, title, 1)
        if starting_money.get().isdigit()
        else None,
    )
    title_button.pack()


def info_frame(global_root):
    info = Frame(global_root, bg="Black")
    info.pack(side="bottom", fill="both")

    # TODO: there must be a better way to do this. spaghetti code
    win_count = Label(info, text="Wins: ", bg="Black", fg="White")
    win_count.grid(row=0, column=0)
    win_count_num = Label(info, textvariable=global_wins, bg="Black", fg="White")
    win_count_num.grid(row=0, column=1)

    loss_count = Label(info, text="Losses: ", bg="Black", fg="White")
    loss_count.grid(row=0, column=2)
    loss_count_num = Label(info, textvariable=global_losses, bg="Black", fg="White")
    loss_count_num.grid(row=0, column=3)

    tie_count = Label(info, text="Ties: ", bg="Black", fg="White")
    tie_count.grid(row=0, column=4)
    tie_count_num = Label(info, textvariable=global_ties, bg="Black", fg="White")
    tie_count_num.grid(row=0, column=5)

    money_count = Label(info, text="Money: ", bg="Black", fg="White")
    money_count.grid(row=1, column=0)
    money_count_num = Label(info, textvariable=global_money, bg="Black", fg="White")
    money_count_num.grid(row=1, column=1)


# start the game - call title frame
title_frame(root)

# window mainloop for root object
root.mainloop()
