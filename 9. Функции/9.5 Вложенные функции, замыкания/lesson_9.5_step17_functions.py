def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a * x ** 2 + b * x + c

    return square_polynom
