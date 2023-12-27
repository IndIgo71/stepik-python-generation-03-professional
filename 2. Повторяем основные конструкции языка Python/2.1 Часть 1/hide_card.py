def hide_card(card_number):
    return '*' * 12 + ''.join(card_number.split())[-4:]
