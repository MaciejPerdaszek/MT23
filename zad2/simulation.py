import getopt
import math
import random
import sys


# simulated annealing - searching for global maximum
def simulated_annealing(function, temperature, cooling_parameter, boltzmann_k, max_iterations, max_eras):
    era_number = 0  # No of eras
    solution = random.uniform(function.LOWER_RANGE, function.UPPER_RANGE)
    while True:
        for i in range(max_iterations):
            random_solution = random.uniform(function.LOWER_RANGE, function.UPPER_RANGE)
            diff = function.value(solution) - function.value(random_solution)
            if diff < 0:  # new result is better
                solution = random_solution
            else:
                p = random.uniform(0, 1)
                if p < math.exp(-diff / (boltzmann_k * temperature)):
                    solution = random_solution  # worse solution accepted
        temperature *= cooling_parameter
        era_number += 1
        # stop condition (based on number of eras)
        if era_number == max_eras:
            break
    return solution


class Function1:
    ID = 1
    LOWER_RANGE = -150
    UPPER_RANGE = 150

    @staticmethod
    def value(x):
        if -105 < x < -95:
            return -2 * abs(x + 100) + 10
        elif 95 < x < 105:
            return -2.2 * abs(x - 100) + 11
        else:
            return 0


class Function2:
    ID = 2
    LOWER_RANGE = -1
    UPPER_RANGE = 2

    @staticmethod
    def value(x):
        return x * math.sin(10 * math.pi * x) + 1


functionArg = None
temperatureArg = None
coolingArg = None
boltzmannArg = None
iterationsArg = None
erasArg = None

argumentList = sys.argv[1:]
options = "12t:c:k:i:e:"
long_options = ["Function_1", "Function_2", "Temperature=", "Cooling=", "Boltzmann=", "Iterations=", "Eras="]

try:
    args, values = getopt.getopt(argumentList, options, long_options)
    for currArg, currVal in args:

        if currArg in ("-1", "--Function_1"):
            functionArg = Function1()

        elif currArg in ("-2", "--Function_2"):
            functionArg = Function2()

        elif currArg in ("-t", "--Temperature"):
            temperatureArg = float(currVal)

        elif currArg in ("-c", "--Cooling"):
            coolingArg = float(currVal)

        elif currArg in ("-k", "--Boltzmann"):
            boltzmannArg = float(currVal)

        elif currArg in ("-i", "--Iterations"):
            iterationsArg = int(currVal)

        elif currArg in ("-e", "--Eras"):
            erasArg = int(currVal)

except getopt.error as err:
    print(str(err))

if functionArg and temperatureArg and coolingArg and boltzmannArg and iterationsArg and erasArg:
    result = simulated_annealing(functionArg, temperatureArg, coolingArg, boltzmannArg, iterationsArg, erasArg)
    print(str(result) + ";" + str(functionArg.value(result)))
else:
    print("Invalid arguments")
