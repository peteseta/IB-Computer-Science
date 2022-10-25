import random

TRIES = 10

guess = 0
tries_left = TRIES
correct = 0


def feedback(guess, num):
    feedback = ""
    # loop through each digit in the guess.
    # if the digit is in the correct place, add R to feedback.
    # if the digit is in the num but in the wrong place, add Y to feedback.
    # # if the digit is not in the num, add B to feedback.
    for pos, char in enumerate(guess):
        if char in num:
            if char == num[pos]:
                feedback += "R"
            else:
                feedback += "Y"
        else:
            feedback += "B"
    return feedback


def make_guess():
    while True:
        guess = input("Enter your four digit guess: ")
        if len(guess) == 4:
            break
        print("The guess must be 4 digits!")
    return str(guess)


num = str(random.randint(1000, 9999))

# core gameplay loop
while tries_left > 0:
    # lets the user make a guess
    print(f"You have {tries_left} tries left!")
    guess = make_guess()

    # if the guess is right then break to return a congrats
    if guess == num:
        correct = 1
        break

    # if the guess is wrong, then give feedback
    print(feedback(guess, num))
    tries_left -= 1

# print the end statement
if correct:
    print("You guessed it! The number was", num)
else:
    print("Sorry, skill issue, the number was ", num)
