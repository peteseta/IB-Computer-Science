from random import randint

grid = []

# A procedure to generate/shake a new 4 by 4 grid of 16 dice
def resetGrid():
    global grid
    grid = []
    for row in range(4):
        grid.append([])
        for col in range(4):
            dice = randint(1, 6)
            grid[row].append(dice)


# A procedure to display the dice grid
def displayGrid():
    global grid
    for row in range(4):
        st = "| "
        for col in range(4):
            st = st + str(grid[row][col]) + " | "
        print(st)


# A function to check if a number is an even number
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


# A function to check if a number is an odd number
def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False


# Scoring Functions
# Check corners for all odd or even
def checkCorners():
    check_score = 0
    if (
        isEven(grid[0][0])
        and isEven(grid[0][3])
        and isEven(grid[3][0])
        and isEven(grid[3][3])
    ):
        print("Four even corners! +20pts")
        check_score += 20
    elif (
        isOdd(grid[0][0])
        and isOdd(grid[0][3])
        and isOdd(grid[3][0])
        and isOdd(grid[3][3])
    ):
        print("Four odd corners! +20pts")
        check_score += 20

    return check_score


# Check L to R and R to L diagonals for all odd or even
def checkDiagonal():
    check_score = 0
    if (
        isEven(grid[0][0])
        and isEven(grid[1][1])
        and isEven(grid[2][2])
        and isEven(grid[3][3])
    ):
        print("Four evens in a diagonal! +20pts")
        check_score += 20
    elif (
        isEven(grid[0][3])
        and isEven(grid[1][2])
        and isEven(grid[2][1])
        and isEven(grid[3][0])
    ):
        print("Four evens in a diagonal! +20pts")
        check_score += 20
    elif (
        isOdd(grid[0][0])
        and isOdd(grid[1][1])
        and isOdd(grid[2][2])
        and isOdd(grid[3][3])
    ):
        print("Four odds in a diagonal! +20pts")
        check_score += 20
    elif (
        isOdd(grid[0][3])
        and isOdd(grid[1][2])
        and isOdd(grid[2][1])
        and isOdd(grid[3][0])
    ):
        print("Four odds in a diagonal! +20pts")
        check_score += 20

    return check_score


# Check rows for all odd or even
def checkRows():
    check_score = 0
    for row in range(4):
        if (
            isEven(grid[row][0])
            and isEven(grid[row][1])
            and isEven(grid[row][2])
            and isEven(grid[row][3])
        ):
            print("A row with all evens! +20pts")
            check_score += 20
        elif (
            isOdd(grid[row][0])
            and isOdd(grid[row][1])
            and isOdd(grid[row][2])
            and isOdd(grid[row][3])
        ):
            print("A row with all odds! +20pts")
            check_score += 20
    return check_score


# Check columns for all odd or even
def checkColumns():
    check_score = 0
    for col in range(4):
        if (
            isEven(grid[0][col])
            and isEven(grid[1][col])
            and isEven(grid[2][col])
            and isEven(grid[3][col])
        ):
            print("A column with all odds! +20pts")
            check_score += 20
        elif (
            isOdd(grid[0][col])
            and isOdd(grid[1][col])
            and isOdd(grid[2][col])
            and isOdd(grid[3][col])
        ):
            print("A column with all odds! +20pts")
            check_score += 20
    return check_score


# sum of all dice
def diceScore():
    dice_score = 0

    for row in range(4):
        for col in range(4):
            dice_score += grid[row][col]

    print(f"Sum of all dice is {dice_score}! +{dice_score}pts")
    return dice_score


# Main program
resetGrid()
displayGrid()
score = 0

print("\n" + "Scoring..." + "\n")

score = checkCorners() + checkDiagonal() + checkRows() + checkColumns() + diceScore()

print("\nGrid score: " + str(score) + " pts.")
