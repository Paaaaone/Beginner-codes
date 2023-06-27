import random


class Dice:
    def roll(self):
        number = [0, 0]
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1, d2


roll1 = Dice()
print(roll1.roll())
