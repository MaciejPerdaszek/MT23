import random

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
            weight_sum += objects[i][1]
            value_sum += objects[i][2]
    if weight_sum > max_weight:
        return 0
    return value_sum


def fitness_score_sum(population) -> int:
    fitness_sum = 0
    for individual in population:
        fitness_sum += fitness_score(individual)
    return fitness_sum


def population_probability(population) -> []:
    probabilities = []
    fitness_sum = fitness_score_sum(population)

    for individual in population:
        probabilities.append(fitness_score(individual) / fitness_sum)

    return probabilities


def roulette_selection(population, number_of_chosen):
    selected = []
    population_prob = population_probability(population)
    max_range = sum(population_prob)

    for i in range(number_of_chosen):
        pick = random.uniform(0, max_range)
        current = 0
        for j in range(len(population)):
            current += population_prob[j]
            if current > pick:
                selected.append(population[j])

    return selected


def crossover(parent_a: list, parent_b: list, crossover_points: list) -> []:
    children = [[], []]
    prev = 0
    if (crossover_points[len(crossover_points)] < len(parent_a)
            and crossover_points[len(crossover_points)] < len(parent_b)):

        for i in range(len(crossover_points)):
            crossover_point = crossover_points[i]
            children[0].append(parent_a[prev:crossover_point])
            children[1].append(parent_b[prev:crossover_point])
            prev += crossover_point
            parent_a, parent_b = parent_b, parent_a

    return children


def mutation(individual: list) -> []:
    individual_length = len(individual)
    random_index = random.randint(0, individual_length)
    if individual[random_index] == 0:
        individual[random_index] = 1
    elif individual[random_index] == 1:
        individual[random_index] = 0

    return individual


def genetic_algorithm(population_size: int, number_of_generations: int,
                      selection_method, crossover_points: list, mutation_parameter: float) -> []:
    best_fitness = 0
    best_generation = []
    global_population = init_population(population_size, number_of_generations)

    for generation in range(number_of_generations):
        current_fitness = fitness_score_sum(global_population)
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_generation = global_population

        chosen: list = selection_method(global_population, population_size)
        children = []
        i = 0
        while i < len(chosen):
            j = i
            parent_a = chosen[i]
            while j < len(chosen):
                parent_b = chosen[j]
                for child in crossover(parent_a, parent_b, crossover_points):
                    children.append(child)
        for i in range(len(children)):
            p = random.uniform(0, 1)
            if p < mutation_parameter:
                children[i] = mutation(children[i])

        for child in children:
            chosen.append(child)

        global_population = selection_method(chosen, population_size)

    return best_generation
