from random import randint
from tkinter import Button, Frame, Label, StringVar, Tk

# returns sum of two random integers 1-6 inclusive (2 dice roll)
def roll_dice():
    return randint(1, 6) + randint(1, 6)


# at this point, the user has won or lost the game
def end_screen_frame(global_root, source):
    # destroys the preceding frame; either the point frame or the come out roll frame depending when the user wins/loses
    source.destroy()

    # handles quitting the game (if they don't want to play again)
    def quit_game():
        print("quitting --------")
        exit()

    # handles restarting the game (if they want to play again)
    def new_game():
        print("starting new game -------")
        make_bet_frame(global_root, end_screen)

    # frame for the end screen
    end_screen = Frame(global_root)
    end_screen.pack(side="top", expand=True, fill="both")

    game_over = Label(end_screen, text="Game Over. Do you want to play again?")
    game_over.grid(row=0, column=1)

    # prompt user to play again.
    # if they click yes then go back to the make bet screen.
    play_again = Button(end_screen, text="Yes", command=lambda: new_game())
    play_again.grid(row=1, column=0)

    # quit the game by calling quit_game() if the user clicks no.
    end_game = Button(end_screen, text="No", command=lambda: quit_game())
    end_game.grid(row=1, column=2)


def point_frame(global_root, come_out_roll, point):
    # destroy the come out roll frame
    come_out_roll.destroy()

    # the point is set as the result of the come out roll (passed into this func)
    # tkinter acts weird if the global variable 'point' is used hence a copy is made. idk why either.
    target_point = point
    print("point loop: point is " + str(target_point))

    # init blank variable for displaying the result of the roll
    result_text_var = StringVar()
    result_text_var.set("")

    # handles rolling: roll the dice and depending on the bet update the result
    def calculate_point_roll(dice):
        if dice == 7:
            if bet == 0:
                # win
                result_text_var.set("You win!")
                return 1
            else:
                # lose
                result_text_var.set("You lose!")
                return 0
        elif dice == target_point:
            if bet == 0:
                # lose
                result_text_var.set("You lose!")
                return 0
            else:
                # win
                result_text_var.set("You win!")
                return 1
        elif bet == 1:
            # need to get point
            result_text_var.set(
                "Keep going. You have to roll a " + str(target_point) + "!"
            )
            return 2
        elif bet == 0:
            # need to get a 7
            result_text_var.set("Keep going. You have to roll a 7!")
            return 3

    # based on the result of the roll, update the result text and prompt the user to roll again or go to the end screen
    def point_roll():
        dice = roll_dice()
        result = calculate_point_roll(dice)

        # replacing the title with the number the player rolls
        point_title.destroy()
        roll_text = "You rolled a " + str(dice) + "!"
        roll_result = Label(point, text=roll_text)
        roll_result.grid(row=0, column=2)

        # if there is a win or loss, destroy the roll button and prompt the user to go to end_screen
        if result == 0 or result == 1:
            print("win!" if result == 1 else "lose!")
            point_button.destroy()
            point_next = Button(
                point, text="Next", command=lambda: end_screen_frame(global_root, point)
            )
            point_next.grid(row=1, column=2)

    # create frame for the point loop
    point = Frame(global_root)
    point.pack(side="top", expand=True, fill="both")

    # shows what the point is (the number that was rolled initally)
    title_text = "Keep rolling! The point is " + str(target_point) + "."
    point_title = Label(point, text=title_text)
    point_title.grid(row=0, column=2)

    # button to roll
    point_button = Button(point, text="Roll", command=lambda: point_roll())
    point_button.grid(row=1, column=2)

    # label updated with result of the roll once rolled
    # e.g. a win or loss, or a prompt to keep rolling and that the user has to roll the point or a 7 (based on bet)
    point_result = Label(point, textvariable=result_text_var)
    point_result.grid(row=2, column=2)


def come_out_roll_frame(global_root, make_bet):
    # destroy the bet screen
    make_bet.destroy()

    # init label to prompt the user to roll. will later update with what was rolled.
    rolled_text_var = StringVar()
    rolled_text_var.set("Roll the dice!")

    # init label to show the result of the roll. will later update with the result of the roll.
    result_text_var = StringVar()
    result_text_var.set("")

    # calculate result of the come out roll based on bet type and roll
    def calculate_first_roll(dice):
        if bet == 1:
            if dice == 7 or dice == 11:
                # win
                result_text_var.set("You win!")
                return 1
            elif dice == 2 or dice == 3 or dice == 12:
                # lose
                result_text_var.set("You lose!")
                return 0
            else:
                # point
                result_text_var.set("Point!")
                return 3
        elif bet == 0:
            if dice == 2 or dice == 3:
                # win
                result_text_var.set("You win!")
                return 1
            elif dice == 7 or dice == 11:
                # lose
                result_text_var.set("You lose!")
                return 0
            elif dice == 12:
                # tie
                result_text_var.set("Tie!")
                return 2
            else:
                # point
                result_text_var.set("Point!")
                return 3

    # first roll of dice, on the initial press of the button. the dice is rolled and the result is shown to the user.
    def first_roll():
        # roll the dice and show the result
        dice = roll_dice()
        rolled_text_var.set("You rolled a " + str(dice) + "!")

        # calculate result of the roll
        result = calculate_first_roll(dice)

        # destroy the title and button as there is only one first roll.
        come_out_roll_button.destroy()
        come_out_roll_title.destroy()

        # create a new label to show the result with description
        come_out_roll_result = Label(come_out_roll, textvariable=result_text_var)
        come_out_roll_result.grid(row=3, column=2)

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

    # create frame for the come out roll
    come_out_roll = Frame(global_root)
    come_out_roll.pack(side="top", expand=True, fill="both")

    come_out_roll_title = Label(come_out_roll, text="Time for the come out roll!")
    come_out_roll_title.grid(row=0, column=2)

    # button to roll for the first time. calls first_roll()
    come_out_roll_button = Button(
        come_out_roll, text="Roll", command=lambda: first_roll()
    )
    come_out_roll_button.grid(row=1, column=2)

    come_out_roll_label = Label(come_out_roll, textvariable=rolled_text_var)
    come_out_roll_label.grid(row=2, column=2)


def make_bet_frame(global_root, source):
    # destroy the source screen:
    # either the title if this is the first game or the end_screen if the user is playing again
    source.destroy()

    # handles making the bet - Pass Line
    def pass_line(global_root, make_bet):
        global bet
        bet = 1
        print("pass line set")
        come_out_roll_frame(global_root, make_bet)

    # handles making the bet - No Pass Line
    def no_pass_line(global_root, make_bet):
        global bet
        bet = 0
        print("no pass line set")
        come_out_roll_frame(global_root, make_bet)

    # create frame for bet placing screen
    make_bet = Frame(global_root)
    make_bet.pack(side="top", expand=True, fill="both")

    # prompt user to make bet
    make_bet_label = Label(make_bet, text="Make your bet!")
    make_bet_label.grid(row=0, column=3)

    # button to make pass line bet
    make_bet_button_pass = Button(
        make_bet, text="Pass Line", command=lambda: pass_line(global_root, make_bet)
    )
    make_bet_button_pass.grid(row=1, column=2)

    # button to make no pass line bet
    make_bet_button_nopass = Button(
        make_bet,
        text="No Pass Line",
        command=lambda: no_pass_line(global_root, make_bet),
    )
    make_bet_button_nopass.grid(row=1, column=4)


def title_frame(global_root):
    # create title screen frame
    title = Frame(global_root)
    title.pack(side="top", expand=True, fill="both")

    # title text
    title_label = Label(title, text='Welcome to Crap Craps. To start, press "Play"')
    title_label.pack()

    # button to start game
    title_button = Button(
        title, text="Play", command=lambda: make_bet_frame(global_root, title)
    )
    title_button.pack()


# init window and set size
app_title = "Crap Craps v0.3"
root = Tk(className=app_title)
root.geometry("400x200")

# start the game - call title frame
title_frame(root)

# window mainloop
root.mainloop()
