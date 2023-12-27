class PowerOf:
    def __init__(self, number):
        self.number = number
        self.power = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.number ** self.power
        self.power += 1
        return result
