import getopt
import sys

import genetic_algorithm

argumentList = sys.argv[1:]
options = "p:g:m:"
long_options = ["PopulationSize=", "NumberOfGenerations=", "Roulette", "CrossoverPoints=", "MutationParameter="]

population_size = None
number_of_generations = None
selection_method = None
crossover_points = []
mutation_parameter = None

try:
    args, values = getopt.getopt(argumentList, options, long_options)
    for currArg, currVal in args:

        if currArg in ("-p", "--PopulationSize"):
            population_size = int(currVal)

        elif currArg in ("-g", "--NumberOfGenerations"):
            number_of_generations = int(currVal)

        elif currArg in ("-m", "--MutationParameter"):
            mutation_parameter = float(currVal)

        elif currArg in "--Roulette":
            selection_method = genetic_algorithm.roulette_selection

        elif currArg in "--CrossoverPoints":
            string = currVal.split(',')
            for s in string:
                crossover_points.append(int(s))
except getopt.error as err:
    print(str(err))

if population_size and number_of_generations and mutation_parameter and selection_method and len(crossover_points) > 0:
    objects = []
    file = open('data.txt', 'R')
    while True:
        line = file.readline()
        if not line:
            break
        o = line.split(';')
        obj = [o[0], int(o[1]), int(o[2])]
        objects.append(obj)
    file.close()

    with open('output.txt', 'w') as out:
        out.write(genetic_algorithm
                  .genetic_algorithm(population_size, number_of_generations,
                                     selection_method, crossover_points, mutation_parameter))

else:
    print("Invalid arguments")
