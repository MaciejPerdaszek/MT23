import argparse
import random

from data_structure import IndividualSolution
from load_data import get_customers_from_file, get_vehicle_data
from GA import genetic_algorithm
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Zad 6')
parser.add_argument('-f', '--file', type=str, required=True, help='File name')
parser.add_argument('-p', '--population', type=int, required=True, help='Population size')
parser.add_argument('-g', '--generations', type=int, required=True, help='Number of generations')
parser.add_argument('-m', '--mutation', type=float, required=True, help='Mutation rate')
parser.add_argument('-c', '--crossover', type=float, required=True, help='Crossover rate')
parser.add_argument('-t', '--two-opt', action='store_true', help='Use two opt')
parser.add_argument('-r', '--roulette', action='store_true', help='Use roulette selection')
parser.add_argument('-e', '--elitism', action='store_true', help='Use elitism selection')
parser.add_argument('-nv', '--number-of-vehicles', type=int, required=True, help='Number of vehicles')

args = parser.parse_args()

file_name = args.file
population_size = args.population
number_of_generations = args.generations
mutation_rate = args.mutation
crossover_rate = args.crossover
use_two_opt = args.two_opt
nv = args.number_of_vehicles

customers = get_customers_from_file(file_name)
vehicle_data = get_vehicle_data()
group = file_name[:2]
vehicle_capacity = vehicle_data[group]

if args.roulette:
    selection = 'roulette'
elif args.elitism:
    selection = 'elitism'
else:
    print('You have to choose selection method')
    exit(1)

best_generation, best_generation_fitness = genetic_algorithm(customers, vehicle_capacity, nv, population_size,
                                                             number_of_generations, mutation_rate, crossover_rate,
                                                             use_two_opt,
                                                             selection)

# print('Best generation fitness: ' + str(best_generation_fitness))
print("")
print('Distance: ' + str(round(best_generation.get_best_solution().distance(), 2)))
print('NV: ' + str(len(best_generation.get_best_solution().routes)))


def generate_solution_plot(solution: IndividualSolution):
    plt.figure(figsize=(8, 8))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for route in solution.routes:
        color = random.choice(colors)
        for i in range(len(route.customers) - 1):
            customer_start = route.customers[i]
            customer_end = route.customers[i + 1]

            x_start, y_start = customer_start.x, customer_start.y
            x_end, y_end = customer_end.x, customer_end.y

            plt.plot([x_start, x_end], [y_start, y_end], linestyle='dashed', color=color)

    for route in solution.routes:
        for customer in route.customers:
            plt.plot(customer.x, customer.y, marker='o', color='blue')

    plt.title('Best solution')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    plt.show()

#generate_solution_plot(best_generation.get_best_solution())
