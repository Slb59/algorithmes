import random


class DiceGame:
    def __init__(self, num_faces):
        self.num_faces = num_faces

    def roll_dice(self):
        def roll():
            return random.randint(1, self.num_faces)
        return roll


# Create instances of DiceGame
game1 = DiceGame(6)
game2 = DiceGame(10)

# Get the roll functions
roll_dice_game1 = game1.roll_dice()
roll_dice_game2 = game2.roll_dice()

# Roll the dice
print("Rolling a 6-faced die:", roll_dice_game1())    # Output: Random number between 1 and 6
print("Rolling a 6-faced die:", roll_dice_game1())    # Output: Random number between 1 and 6
print("Rolling a 10-faced die:", roll_dice_game2())   # Output: Random number between 1 and 10
print("Rolling a 10-faced die:", roll_dice_game2())   # Output: Random number between 1 and 10