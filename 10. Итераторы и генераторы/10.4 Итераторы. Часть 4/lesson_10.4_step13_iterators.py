class CardDeck:
    def __init__(self):
        self.suit = ("пик", "треф", "бубен", "червей")
        self.value = (
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "валет", "дама", "король", "туз")
        self.counter = -1
        self.cards_count = 52

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= self.cards_count:
            raise StopIteration
        return f'{self.value[self.counter % 13]} {self.suit[self.counter // 13]}'
