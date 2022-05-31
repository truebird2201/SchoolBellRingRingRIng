import random

class Dice:
    def __init__(self):
        self.roll = 0

    def rollDie(self):
        self.roll = random.randint(1, 6)

    def getRoll(self):
        return self.roll
