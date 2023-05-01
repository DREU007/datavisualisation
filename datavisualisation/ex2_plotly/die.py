from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die = Initialize number of sides in the die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)


class Dice(Die):
    def __init__(self, *args):
        if not args:
            args = (6,)
        self.dies = [Die(arg) for arg in args]

    def roll(self):
        return [die.roll() for die in self.dies]

    def multiple_rolls(self, number):
        return [sum(self.roll()) for _ in range(number)]

    def possible_results(self):
        max_sides = sum(die.num_sides for die in self.dies)
        min_sides = len(self.dies)

        return range(min_sides, max_sides + 1)

    def frequencies(self, rolls_result):
        return [rolls_result.count(value) for value in self.possible_results()]
