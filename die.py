from random import randint

class Die():
    "class presents die"

    def __init__(self, num_sides=6):
        'default sides of a die'
        self.num_sides = num_sides

    def roll(self):
        """return a random value between 1 and sides of a die"""
        return randint(1, self.num_sides)
    
