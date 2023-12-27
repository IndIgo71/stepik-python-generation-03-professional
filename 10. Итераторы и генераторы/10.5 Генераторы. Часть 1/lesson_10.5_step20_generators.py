def card_deck(suit):
    suits = ["пик", "треф", "бубен", "червей"]
    suits.remove(suit)
    cards = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "валет", "дама", "король", "туз")
    while True:
        for suit in suits:
            for card in cards:
                yield f'{card} {suit}'
