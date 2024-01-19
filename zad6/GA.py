import copy

from VRPTW import VRPTW


def genetic_algorithm(customers, vehicle_capacity, population_size,
                      number_of_generations, mutation_rate, crossover_rate):
    lib = VRPTW(population_size, vehicle_capacity, customers)
    population = lib.population

    best_generation = copy.deepcopy(population)
    best_generation_fitness = population.fitness_score_sum()

    for generation in range(number_of_generations):
        print('Generation: ' + str(generation))
        population.crossover(crossover_rate)
        population.mutation(mutation_rate)
        population.selection(population_size)

        current_generation_fitness = population.fitness_score_sum()
        if current_generation_fitness < best_generation_fitness:
            best_generation_fitness = current_generation_fitness
            best_generation = copy.deepcopy(population)

    return best_generation, best_generation_fitness
