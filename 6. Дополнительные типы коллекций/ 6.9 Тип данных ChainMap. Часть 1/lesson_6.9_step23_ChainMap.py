from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

products = ChainMap(bread, meat, sauce, vegetables, toppings)
ingredients = Counter(input().split(','))
width = len(max(ingredients, key=len))
total = sum(map(lambda x: products[x] * ingredients[x], ingredients))
total_text = f'ИТОГ: {total}р'

for indigrient, count in sorted(ingredients.items()):
    print(f'{indigrient.ljust(width)} x {count}')
print('-' * max(len(total_text), (width + 3 + len(str(max(ingredients.values()))))))
print(total_text)
