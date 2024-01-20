import math
import random


class Customer:
    def __init__(self, id, x, y, demand, ready_time, due_date, service_time):
        self.id = id
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_time = service_time

    def distance_to(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Route:
    def __init__(self, customers: [Customer]):
        self.customers = customers

    def distance(self) -> float:
        distance = 0
        for i in range(len(self.customers) - 1):
            distance += self.customers[i].distance_to(self.customers[i + 1])
        return distance

    def time_window_penalty(self) -> float:
        time_window_penalty = 0
        time = 0
        for customer in self.customers:
            if time < customer.ready_time:
                time_window_penalty += customer.ready_time - time
            if time > customer.due_date:
                time_window_penalty += time - customer.due_date
            time += customer.service_time
        return time_window_penalty

    def capacity_penalty(self) -> float:
        capacity_penalty = 0
        load = 0
        for customer in self.customers:
            load += customer.demand
        return capacity_penalty

    def two_opt(self):
        improved = True
        while improved:
            improved = False
            for i in range(0, len(self.customers) - 1, 1):
                pair = (self.customers[i], self.customers[i + 1])
                route = self.customers[:]
                route.remove(pair[0])
                route.remove(pair[1])
                route.insert(i, pair[1])
                route.insert(i + 1, pair[0])
                current_route_cost = self.distance()
                new_route_cost = Route(route).distance()
                if new_route_cost < current_route_cost:
                    self.customers = route
                    improved = True


class IndividualSolution:
    def __init__(self, routes: [Route], allCustomers: [Customer]):
        self.routes = routes
        self.allCustomers = allCustomers

    def distance(self) -> float:
        distance = 0
        for route in self.routes:
            distance += route.distance()
        return distance

    def fitness_score(self) -> float:
        total_distance = self.distance()

        time_window_penalty = 0
        for route in self.routes:
            time_window_penalty += route.time_window_penalty()

        capacity_penalty = 0
        for route in self.routes:
            capacity_penalty += route.capacity_penalty()

        unserved_customers_penalty = 0
        for customer in self.allCustomers:
            served = False
            for route in self.routes:
                if customer in route.customers:
                    served = True
                    break
            if not served:
                unserved_customers_penalty += math.inf

        return total_distance + time_window_penalty + capacity_penalty + unserved_customers_penalty

    def two_opt(self):
        for route in self.routes:
            route.two_opt()


class Population:
    def __init__(self, solutions: [IndividualSolution], allCustomers: [Customer]):
        self.solutions = solutions
        self.allCustomers = allCustomers

    def fitness_score_sum(self) -> float:
        fitness_sum = 0
        for solution in self.solutions:
            fitness_sum += solution.fitness_score()
        return fitness_sum

    # Roulette wheel selection
    def roulette_selection(self, number_of_chosen) -> []:
        selected = []
        max_fitness = max(solution.fitness_score() for solution in self.solutions)
        inverted_fitness_values = [max_fitness - solution.fitness_score() for solution in self.solutions]
        total_fitness = sum(inverted_fitness_values)

        for count in range(number_of_chosen):
            rand_num = random.uniform(0, total_fitness)
            cumulative_probability = 0
            for i, fitness in enumerate(inverted_fitness_values):
                cumulative_probability += fitness
                if rand_num <= cumulative_probability:
                    selected.append(self.solutions[i])
                    break

        self.solutions = selected

    def elitism_selection(self, number_of_chosen) -> []:
        self.solutions = sorted(self.solutions, key=lambda solution: solution.fitness_score())
        self.solutions = self.solutions[:number_of_chosen]

    def crossover(self, crossover_rate):
        for i in range(0, len(self.solutions), 2):
            if random.random() < crossover_rate:
                parent1 = self.solutions[i]
                parent2 = self.solutions[i + 1]
                child1 = IndividualSolution([], self.allCustomers)
                child2 = IndividualSolution([], self.allCustomers)

                subset_start = random.randint(0, len(parent1.routes) - 1)
                subset_end = random.randint(subset_start, len(parent1.routes) - 1)

                child1.routes = parent1.routes[subset_start:subset_end]
                child2.routes = parent2.routes[subset_start:subset_end]

                for route in parent2.routes:
                    if route not in child1.routes:
                        child1.routes.append(route)

                for route in parent1.routes:
                    if route not in child2.routes:
                        child2.routes.append(route)

                self.solutions.append(child1)
                self.solutions.append(child2)

    def mutation(self, mutation_rate):
        for solution in self.solutions:
            if random.random() < mutation_rate:
                route = random.choice(solution.routes)
                customers = route.customers
                customer1index = random.randint(0, len(customers) - 1)
                customer2index = random.randint(0, len(customers) - 1)

                customers[customer1index], customers[customer2index] = customers[customer2index], customers[customer1index]

    def two_opt(self):
        for solution in self.solutions:
            solution.two_opt()

    def get_best_solution(self) -> IndividualSolution:
        best_solution = self.solutions[0]
        for solution in self.solutions:
            if solution.fitness_score() < best_solution.fitness_score():
                best_solution = solution
        return best_solution
