def index_of_nearest(numbers, number):
    return numbers.index(min(numbers, key=lambda x: abs(x - number))) if numbers else -1
