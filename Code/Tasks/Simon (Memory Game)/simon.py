# create a simon memory game
# it will have 4 panels which flash colors for the user to remember and then repeat
# on the first round, flash 1 color. each subsequent round, increase the number of colors flashed.
# GUI is created using tkinter. It has 4 buttons, each with a different color: red, green, blue, yellow
# you will also need a button to start a new game and a field for score from the last round

from tkinter import *
from tkmacosx import Button
import random


class Simon:
    def __init__(self):
        window = Tk()
        window.title("Simon")

        self.score = 0

        # create a frame to hold the buttons
        frame1 = Frame(window)
        frame1.pack()
        # create the 4 buttons
        self.red = Button(frame1, text="Red", command=self.redPressed)
        self.red.grid(row=1, column=1)
        self.green = Button(frame1, text="Green", command=self.greenPressed)
        self.green.grid(row=1, column=2)
        self.blue = Button(frame1, text="Blue", command=self.bluePressed)
        self.blue.grid(row=1, column=3)
        self.yellow = Button(frame1, text="Yellow", command=self.yellowPressed)
        self.yellow.grid(row=1, column=4)

        # create a frame to hold the score
        frame2 = Frame(window)
        frame2.pack()
        # create a label to display the score
        self.scoreLabel = Label(frame2, text="Score: " + str(self.score))
        self.scoreLabel.pack()

        # create a frame to hold the new game button
        frame3 = Frame(window)
        frame3.pack()
        # create a button for new game
        self.newGame = Button(
            frame3, text="New Game", command=lambda: self.startNewGame()
        )
        self.newGame.pack()

        # create a list to hold the sequence of colors to be flashed
        self.sequence = []

        # create a variable to hold the current color to be flashed
        self.currentColor = ""

        self.currentColorPressed = ""

        # create a variable to hold the current index in the sequence
        self.currentIndex = 0

        # create a variable to hold the number of colors to be flashed
        self.numberOfColors = 5

        window.mainloop()

    # resets variables and starts a new game
    def startNewGame(self):
        self.score = 0
        self.scoreLabel["text"] = "Score: " + str(self.score)
        self.currentIndex = 0
        self.numberOfColors = 5
        self.flashColors()

    # flash random colors in the sequence
    def flashColors(self):
        self.sequence = []
        for i in range(self.numberOfColors):
            self.sequence.append(random.choice(["red", "green", "blue", "yellow"]))
        for color in self.sequence:
            if color == "red":
                # self.red["bg"] = "red"
                # self.red.after(500)
                # self.red["bg"] = "white"
                self.red.after(200, lambda: self.red.configure(bg="red"))
                self.red.after(750, lambda: self.red.configure(bg="white"))
            elif color == "green":
                # self.green["bg"] = "green"
                # self.green.after(500)
                # self.green["bg"] = "white"
                self.green.after(200, lambda: self.green.configure(bg="green"))
                self.green.after(750, lambda: self.green.configure(bg="white"))
            elif color == "blue":
                # self.blue["bg"] = "blue"
                # self.blue.after(500)
                # self.blue["bg"] = "white"
                self.blue.after(200, lambda: self.blue.configure(bg="blue"))
                self.blue.after(750, lambda: self.blue.configure(bg="white"))
            elif color == "yellow":
                # self.yellow["bg"] = "yellow"
                # self.yellow.after(500)
                # self.yellow["bg"] = "white"
                self.yellow.after(200, lambda: self.yellow.configure(bg="yellow"))
                self.yellow.after(750, lambda: self.yellow.configure(bg="white"))

    # checks the color pressed against the colors in the sequence
    def checkColor(self):
        if self.currentColorPressed == self.sequence[self.currentIndex]:
            self.currentIndex += 1
            if self.currentIndex == self.numberOfColors:
                self.score += 1
                self.scoreLabel["text"] = "Score: " + str(self.score)
                self.currentIndex = 0
                self.numberOfColors += 1
                self.flashColors()
        else:
            self.scoreLabel["text"] = "Score: " + str(self.score)
            self.currentIndex = 0
            self.numberOfColors = 1
            self.flashColors()

    def redPressed(self):
        self.currentColorPressed = "red"
        self.checkColor()

    def greenPressed(self):
        self.currentColorPressed = "green"
        self.checkColor()

    def bluePressed(self):
        self.currentColorPressed = "blue"
        self.checkColor()

    def yellowPressed(self):
        self.currentColorPressed = "yellow"
        self.checkColor()


game = Simon()
