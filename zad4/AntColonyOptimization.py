import random

import Locations
import Ant


def get_best_ant(colony, previous_best_ant):
    best_ant = previous_best_ant
    for ant in colony:
        if best_ant is None:
            best_ant = ant
        elif ant.get_distance() < best_ant.get_distance():
            best_ant = ant
    return best_ant


def update_pheromones(locations: Locations.Locations, colony, evaporation_rate):
    for i in range(len(locations.get_locations())):
        for j in range(len(locations.get_locations())):
            locations.pheromones[i][j] *= evaporation_rate

            for ant in colony:
                locations.pheromones[i][j] += 1 / ant.get_distance()


def initiate_ants(population_size: int, locations: Locations.Locations, alpha: float, beta: float) -> []:
    colony = []
    for i in range(population_size):
        colony.append(Ant.Ant(locations, alpha, beta))
    return colony


def run(locations: Locations.Locations, population_size: int, number_of_iterations: int,
        alpha: float, beta: float, evaporation_rate: float, random_location_probability: float):

    best_ant = None
    for i in range(number_of_iterations):
        print('Iteration: ' + str(i))
        colony = initiate_ants(population_size, locations, alpha, beta)
        for r in range(len(locations.get_locations())):
            for ant in colony:
                if random.random() < random_location_probability:
                    ant.visit_random()
                else:
                    ant.visit_probabilistic()
        update_pheromones(locations, colony, evaporation_rate)
        previous_best_ant = best_ant
        best_ant = get_best_ant(colony, previous_best_ant)
    return best_ant
