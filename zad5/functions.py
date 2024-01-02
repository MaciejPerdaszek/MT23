import math


def get_function(i):
    if i == 1:
        return {'func': function1, 'x_min': -1.5, 'x_max': 4, 'y_min': -3, 'y_max': 4}
    elif i == 2:
        return function2
    else:
        return None


def function1(x, y):
    return math.sin(x + y) + ((x - y) ** 2) - (1.5 * x) + (2.5 * y) + 1


def function2(x, y):
    return 100 * (y - x ** 2) ** 2 + (1 - x) ** 2
