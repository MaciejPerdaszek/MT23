import math
import random
import scipy.constants as sc


# simulated annealing - searching for global maximum
def simulated_annealing(function, lower_range, upper_range, temperature, cooling_parameter, max_iterations, max_eras):
    era_number = 0  # No of eras
    solution = random.uniform(lower_range, upper_range)
    while True:
        for i in range(max_iterations):
            random_solution = random.uniform(solution - (2 * temperature), solution + (2 * temperature))
            if random_solution > upper_range:
                random_solution = upper_range
            elif random_solution < lower_range:
                random_solution = lower_range

            diff = function(solution) - function(random_solution)
            if diff < 0:  # new result is better
                solution = random_solution
            else:
                p = random.uniform(0, 1)
                if p < math.exp(-diff / (sc.Boltzmann * temperature)):
                    solution = random_solution  # worse solution accepted
        temperature *= cooling_parameter
        era_number += 1
        # stop condition (based on number of eras)
        if era_number == max_eras:
            break
    return solution


def function1(x):
    if -105 < x < -95:
        return -2 * abs(x + 100) + 10
    elif 95 < x < 105:
        return -2.2 * abs(x - 100) + 11
    else:
        return 0


def function2(x):
    return x * math.sin(10 * math.pi * x) + 1


print("Function 1:")
f1result = simulated_annealing(function1, -150, 150, 500, 0.999, 3000, 5)
print("x: " + str(f1result) + " y: " + str(function1(f1result)))

print("Function 2:")
f2result = simulated_annealing(function2, -1, 2, 1, 0.997, 1200, 10)
print("x: " + str(f2result) + " y: " + str(function2(f2result)))