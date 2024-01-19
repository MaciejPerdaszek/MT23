import argparse
from zad6.load_data import get_customers_from_file
from zad6.GA import genetic_algorithm

parser = argparse.ArgumentParser(description='Zad 6')
parser.add_argument('-f', '--file', type=str, required=True, help='File name')
parser.add_argument('-v', '--vehicle', type=int, required=True, help='Vehicle capacity')
parser.add_argument('-p', '--population', type=int, required=True, help='Population size')
parser.add_argument('-g', '--generations', type=int, required=True, help='Number of generations')
parser.add_argument('-m', '--mutation', type=float, required=True, help='Mutation rate')
parser.add_argument('-c', '--crossover', type=float, required=True, help='Crossover rate')

args = parser.parse_args()

file_name = args.file
vehicle_capacity = args.vehicle
population_size = args.population
number_of_generations = args.generations
mutation_rate = args.mutation
crossover_rate = args.crossover

customers = get_customers_from_file(file_name)

best_generation, best_generation_fitness = genetic_algorithm(customers, vehicle_capacity, population_size, number_of_generations, mutation_rate, crossover_rate)

print('Best generation fitness: ' + str(best_generation_fitness))
print('Best route distance: ' + str(best_generation.get_best_solution().distance()))

'''#best_generation, best_generation_fitness = genetic_algorithm(customers, vehicle_capacity, population_size,
#                                                             number_of_generations, mutation_rate, crossover_rate)

#print('Best generation fitness: ' + str(best_generation_fitness))
#best_routes, best_distance = get_best_routes(best_generation)
#print('Best routes distance: ' + str(best_distance))
#print('Best routes: ')
#i = 0
for route in best_routes:
    print('Route: ' + str(i), end=' ')
    for customer in route:
        print(customer.id, end=' ')
        print("X " + str(customer.x), end=' ')
        print("Y " + str(customer.y), end=' ')
        print('->', end=' ')
    print()
    i += 1
'''