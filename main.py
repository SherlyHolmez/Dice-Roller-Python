import random

def roll_dice():
    dice_drawing = {
        1: (
            "┌─────────┐",
            "│    1    │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│    2    │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ● 3    │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    4    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ● 5 ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ● 6 ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    roll = input("roll the dice? (Y/N)\n")

    while roll.lower() == "Y".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("Dice rolled: {} and {}".format(dice1,dice2))
        print("\n".join(dice_drawing[dice1] + dice_drawing[dice2]))

        roll = input("Roll again? (Y/N)\n")

roll_dice()