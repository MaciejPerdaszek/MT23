import random

import Locations


class Ant:
    def __init__(self, locations: Locations.Locations, alpha: float, beta: float):
        self.beta = beta
        self.alpha = alpha
        self.visited = []
        self.locations = locations

        rand = random.randint(0, len(self.locations.get_locations()) - 1)
        self.visited.append(self.locations.get_locations()[rand])

    def get_distance(self):
        total_distance = 0
        for i in range(1, len(self.visited)):
            distance = Locations.distance(self.visited[i - 1], self.visited[i])
            total_distance += distance
        return total_distance

    def visit(self):
        pass

    def visit_random(self):
        rand = random.randint(0, len(self.locations.get_locations()) - 1)
        self.visited.append(self.locations.get_locations()[rand])

    def visit_probabilistic(self):
        probabilities = []
        probability_sum = 0
        for location in self.locations.get_locations():
            if location not in self.visited:
                x_pheromones = self.locations.get_pheromone(self.visited[-1], location) ** self.alpha
                x_heuristics = 1 / Locations.distance(self.visited[-1], location) ** self.beta
                probability_sum += x_pheromones * x_heuristics

        for location in self.locations.get_locations():
            if location not in self.visited:
                x_pheromones = self.locations.get_pheromone(self.visited[-1], location) ** self.alpha
                x_heuristics = 1 / Locations.distance(self.visited[-1], location) ** self.beta
                probability = (x_pheromones * x_heuristics) / probability_sum
                probabilities.append({'probability': probability, 'location': location})

        self.roulette_selection(probabilities)

    def roulette_selection(self, probabilities):
        rand = random.random()
        cumulative_probability = 0
        for probability in probabilities:
            prob = probability['probability']
            location = probability['location']
            cumulative_probability += prob
            if rand <= cumulative_probability:
                self.visited.append(location)
                break

