import random
import math


def function1(x):
    if -105 < x < -95:
        return -2 * abs(x + 100) + 10
    elif 95 < x < 105:
        return -2.2 * abs(x - 100) + 11
    else:
        return 0


# print(function1(100.008881))


def simulatedAnnealing(x_start, T, dT, k, M):
    # stop condition?
    for j in range(M):
        x_random = random.uniform(-150, 150)
        dx = function1(x_random) - function1(x_start)
        if dx < 0:
            x_start = x_random
        else:
            x_new = random.uniform(0, 1)
            if x_new < math.exp(-dx / (k * T)):
                x_start = x_random
        T = dT * T
    print("x: " + str(x_start) + "\ny: " + str(function1(x_start)))


simulatedAnnealing(0, 500, 0.999, 0.1, 3000)
