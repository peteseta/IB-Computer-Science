import random
from tkinter import Button, Frame, Label, StringVar, Tk


# returns sum of two random integers 1-6 inclusive (2 dice roll)
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


# at this point, the user has won or lost the game
def end_screen_frame(root, source):
    # destroys the preceding frame; either the point frame or the come out roll frame
    source.destroy()
    print("end screen showing...")

    # handles quitting the game (if they don't want to play again)
    def quit_game():
        print("quitting")
        exit()

    end_screen = Frame(root)
    end_screen.pack(side="top", expand=True, fill="both")

    game_over = Label(end_screen, text="Game Over. Do you want to play again?")
    game_over.grid(row=0, column=1)

    # prompt user to play again.
    # if they click yes then go back to the make bet screen.
    play_again = Button(
        end_screen, text="Yes", command=lambda: make_bet_frame(root, end_screen)
    )
    play_again.grid(row=1, column=0)

    # quit the game by calling quit_game() if the user clicks no.
    end_game = Button(end_screen, text="No", command=lambda: quit_game())
    end_game.grid(row=1, column=2)


def point_frame(root, come_out_roll, point):
    # destroy the come out roll frame
    come_out_roll.destroy()

    # the point is set as the result of the come out roll (passed into this func)
    target_point = point
    print("point loop: point is " + str(target_point))

    # init blank variable for what the user rolled
    result_text_var = StringVar()
    result_text_var.set("")

    # handles rolling: roll the dice and depending on the bet update the result
    def point_roll():
        dice = roll_dice()

        if dice == 7:
            if bet == 0:
                # win
                update_result(1, dice)
            else:
                # lose
                update_result(0, dice)
        elif dice == target_point:
            if bet == 0:
                # lose
                update_result(0, dice)
            else:
                # win
                update_result(1, dice)
        elif bet == 1:
            # need to get point
            update_result(2, dice)
        elif bet == 0:
            # need to get a 7
            update_result(3, dice)

    # based on the result of the roll, update the result text and prompt the user to roll again or go to the end screen
    def update_result(result, dice):

        # text to show to the user based on result
        result_text = (
            "You win!"
            if result == 1
            else "You lose!"
            if result == 0
            else "Keep going. You have to roll a " + str(target_point) + "!"
            if result == 2
            else "Keep going. You have to roll a 7!"
        )
        result_text_var.set(result_text)

        # replacing the title with what the player rolled
        point_title.destroy()
        roll_text = "You rolled a " + str(dice) + "!"
        roll_result = Label(point, text=roll_text)
        roll_result.grid(row=0, column=2)

        # if there is a win or loss, destroy the roll button and prompt the user to go next
        if result == 0 or result == 1:
            point_button.destroy()
            point_next = Button(
                point, text="Next", command=lambda: end_screen_frame(root, point)
            )
            point_next.grid(row=1, column=2)

    point = Frame(root)
    point.pack(side="top", expand=True, fill="both")

    title_text = "Keep rolling! The point is " + str(target_point) + "."
    point_title = Label(point, text=title_text)
    point_title.grid(row=0, column=2)

    point_button = Button(point, text="Roll", command=lambda: point_roll())
    point_button.grid(row=1, column=2)

    point_result = Label(point, textvariable=result_text_var)
    point_result.grid(row=2, column=2)


def come_out_roll_frame(root, make_bet):
    # destroy the bet screen
    make_bet.destroy()

    # calculate output of the come out roll
    def calculate_first_roll(dice):
        if bet == 1:
            if dice == 7 or dice == 11:
                # win
                return 1
            elif dice == 2 or dice == 3 or dice == 12:
                # lose
                return 0
            else:
                # point
                return 3
        elif bet == 0:
            if dice == 2 or dice == 3:
                # win
                return 1
            elif dice == 7 or dice == 11:
                # lose
                return 0
            elif dice == 12:
                # tie
                return 2
            else:
                # point
                return 3

    # handles flow: if the game has been won, go to end screen. if there is a point go to the point frame.
    def next(type, dice):
        if type == 0 or type == 1 or type == 2:
            end_screen_frame(root, come_out_roll)
        else:
            point_frame(root, come_out_roll, dice)

    # shows the result of the come out roll based on bet type and rolled number
    def update_result(dice):
        result = calculate_first_roll(dice)
        print("result: " + str(result))

        come_out_roll_button.destroy()
        come_out_roll_title.destroy()

        resultText = (
            "You win!"
            if result == 1
            else "You lose!"
            if result == 0
            else "Tie!"
            if result == 2
            else "Point!"
        )
        come_out_roll_result = Label(come_out_roll, text=resultText)
        come_out_roll_result.grid(row=3, column=2)

        come_out_roll_next = Button(
            come_out_roll, text="Next", command=lambda: next(result, dice)
        )
        come_out_roll_next.grid(row=4, column=2)

    # first roll of dice
    def first_roll():
        # roll the dice
        dice = roll_dice()

        # show result of the dice roll
        resultText = "You rolled a " + str(dice) + "!"
        come_out_roll_label.configure(text=resultText)

        # prompt to show result and go next
        update_result(dice)

    come_out_roll = Frame(root)
    come_out_roll.pack(side="top", expand=True, fill="both")

    come_out_roll_title = Label(come_out_roll, text="Time for the come out roll!")
    come_out_roll_title.grid(row=0, column=2)

    come_out_roll_button = Button(
        come_out_roll, text="Roll", command=lambda: first_roll()
    )
    come_out_roll_button.grid(row=1, column=2)

    come_out_roll_label = Label(come_out_roll, text="Roll the dice!")
    come_out_roll_label.grid(row=2, column=2)


def make_bet_frame(root, title):
    # destroy the title screen
    title.destroy()

    # handles making the bet - Pass Line
    def pass_line(root, make_bet):
        global bet
        bet = 1
        print("pass set " + str(bet))
        come_out_roll_frame(root, make_bet)

    # handles making the bet - No Pass Line
    def no_pass_line(root, make_bet):
        global bet
        bet = 0
        print("no pass set " + str(bet))
        come_out_roll_frame(root, make_bet)

    # prompt user to make bet
    make_bet = Frame(root)
    make_bet.pack(side="top", expand=True, fill="both")

    make_bet_label = Label(make_bet, text="Make your bet!")
    make_bet_label.grid(row=0, column=3)

    make_bet_button_pass = Button(
        make_bet, text="Pass Line", command=lambda: pass_line(root, make_bet)
    )
    make_bet_button_pass.grid(row=1, column=2)

    make_bet_button_nopass = Button(
        make_bet, text="No Pass Line", command=lambda: no_pass_line(root, make_bet)
    )
    make_bet_button_nopass.grid(row=1, column=4)


def title(root):
    # create title screen frame
    title = Frame(root)
    title.pack(side="top", expand=True, fill="both")

    # title text
    title_label = Label(title, text='Welcome to Crap Craps. To start, press "Play"')
    title_label.pack()

    # button to start game
    title_button = Button(
        title, text="Play", command=lambda: make_bet_frame(root, title)
    )
    title_button.pack()


# init window and set size
root = Tk(className="Crap Craps v0.1")
root.geometry("400x200")

# start the game - call title frame
title(root)

# window mainloop
root.mainloop()
