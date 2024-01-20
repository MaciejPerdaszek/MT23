import copy

from VRPTW import VRPTW


def genetic_algorithm(customers, vehicle_capacity, nv, population_size,
                      number_of_generations, mutation_rate, crossover_rate,
                      use_two_opt,
                      selection):
    lib = VRPTW(population_size, vehicle_capacity, nv, customers)
    population = lib.population

    best_generation = copy.deepcopy(population)
    best_generation_fitness = population.fitness_score_sum()

    for generation in range(number_of_generations):
        #print(' G: ' + str(generation), end=' ')

        population.crossover(crossover_rate)

        population.mutation(mutation_rate)

        if selection == 'roulette':
            population.roulette_selection(population_size)
        elif selection == 'elitism':
            population.elitism_selection(population_size)

        if use_two_opt:
            population.two_opt()

        current_generation_fitness = population.fitness_score_sum()
        if current_generation_fitness < best_generation_fitness:
            best_generation_fitness = current_generation_fitness
            best_generation = copy.deepcopy(population)

    return best_generation, best_generation_fitness
