import random


def scare():
    head = random.choice(["dragon", "lion", "giant"])
    skin = random.choice(["scales", "fur"])
    eyes = random.choice(["blood red", "deep blue", "toxic green"])
    teeth = str(random.randint(5, 25))

    print(
        f"The Gruffalo has the head of a {head}, has {skin} for skin, has {teeth} razor sharp teeth right below its {eyes} eyes."
    )


scare()
