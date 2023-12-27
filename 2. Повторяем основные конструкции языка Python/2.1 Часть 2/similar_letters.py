def is_similar_letters(*args):
    if set('AaBCcEeHKMOoPpTXxy').issuperset(set(args)):
        return 'en'
    elif set('АаВСсЕеНКМОоРрТХху').issuperset(set(args)):
        return 'ru'
    else:
        return 'mix'


l1, l2, l3 = [input() for _ in range(3)]
print(is_similar_letters(l1, l2, l3))
