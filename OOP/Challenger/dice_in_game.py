from random import *

class Dice:
    def __init__(self, sides) -> None:
        self.sides = sides
    
    def roll_dice(self):
        return randint(1, self.sides)

d1 = Dice(6)

print(d1.roll_dice())
print(d1.roll_dice())