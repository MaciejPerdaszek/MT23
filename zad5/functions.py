import math


def get_function(i):
    if i == 1:
        return {'func': function1, 'x_min': -1.5, 'x_max': 4, 'y_min': -3, 'y_max': 4}
    elif i == 2:
        return {'func': function2, 'x_min': -10, 'x_max': 10, 'y_min': -10, 'y_max': 10}
    else:
        return None


def function1(x, y):
    return math.sin(x + y) + ((x - y) ** 2) - (1.5 * x) + (2.5 * y) + 1


def function2(x, y):
    return (math.sin(3*math.pi*x)**2) + ((x - 1)**2) * (1 + (math.sin(3*math.pi*y)**2)) + ((y - 1)**2) * (1 + (math.sin(2*math.pi*y)**2))
