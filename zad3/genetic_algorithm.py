import random
import copy

objects = []
max_weight = 0


def init_population(population_size, individual_size) -> []:
    population = []
    for i in range(population_size):
        individual = []
        for j in range(individual_size):
            individual.append(random.randint(0, 1))
        population.append(individual)
    return population


def fitness_score(individual) -> int:
    weight_sum = 0
    value_sum = 0
    for i in range(len(individual)):
        value = individual[i]
        if value == 1:
            weight_sum += int(objects[i][1])
            value_sum += int(objects[i][2])
    if weight_sum > max_weight:
        return 0
    return value_sum


def fitness_score_sum(population) -> int:
    fitness_sum = 0
    for individual in population:
        fitness_sum += fitness_score(individual)
    return fitness_sum


def roulette_selection(population, number_of_chosen) -> []:
    selected = []
    total_fitness = fitness_score_sum(population)
    if total_fitness != 0:
        fitness_values = []
        for individual in population:
            fitness_values.append(fitness_score(individual))
        selection_probabilities = [fitness / total_fitness for fitness in fitness_values]

        for count in range(number_of_chosen):
            rand_num = random.random()
            cumulative_probability = 0
            for i, prob in enumerate(selection_probabilities):
                cumulative_probability += prob
                if rand_num <= cumulative_probability:
                    selected.append(population[i])
                    break

        return selected


def elitism_selection(population, number_of_chosen) -> []:
    selected = []
    sorted_population = sorted(population, key=lambda x: fitness_score(x), reverse=True)
    for i in range(number_of_chosen):
        selected.append(sorted_population[i])
    return selected


def crossover(parent_a: list, parent_b: list, crossover_points: list, crossover_rate: float) -> []:
    children = [[], []]
    r = random.uniform(0, 1)
    if r < crossover_rate:
        prev = 0
        for i in range(len(crossover_points)):
            crossover_point = crossover_points[i]
            children[0].extend(parent_a[prev:crossover_point])
            children[1].extend(parent_b[prev:crossover_point])
            prev += crossover_point
            parent_a, parent_b = parent_b, parent_a

        children[0].extend(parent_a[prev:])
        children[1].extend(parent_b[prev:])
        return children


def mutation(individual: list, mutation_rate: float) -> []:
    r = random.uniform(0, 1)
    if r < mutation_rate:
        individual_length = len(individual)
        random_index = random.randint(0, individual_length - 1)
        if individual[random_index] == 0:
            individual[random_index] = 1
        elif individual[random_index] == 1:
            individual[random_index] = 0

    return individual


def genetic_algorithm(population_size: int, number_of_generations: int,
                      selection_method, crossover_points: list, mutation_rate: float, crossover_rate: float) -> []:

    global_population = init_population(population_size, len(objects))
    best_fitness = fitness_score_sum(global_population)
    best_generation = global_population

    for generation in range(number_of_generations):

        chosen: list = selection_method(global_population, population_size)
        children = []
        i = 1
        while i < len(chosen):
            parent_a = chosen[i - 1]
            parent_b = chosen[i]

            cr = crossover(parent_a, parent_b, crossover_points, crossover_rate)
            if cr:
                for child in cr:
                    children.append(child)
            i += 2

        for i in range(len(children)):
            children[i] = mutation(children[i], mutation_rate)

        for child in children:
            global_population.append(child)

        global_population = selection_method(global_population, population_size)

        current_fitness = fitness_score_sum(global_population)
        print(current_fitness)
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_generation = copy.deepcopy(global_population)

    print("Return generation " + str(best_fitness) + " " + str(len(best_generation)))
    return best_generation
