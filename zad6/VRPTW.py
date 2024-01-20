import random

from data_structure import Population, Route, Customer, IndividualSolution


class VRPTW:
    def __init__(self, population_size, vehicle_capacity, nv, customers: [Customer]):
        self.vehicle_capacity = vehicle_capacity
        self.population_size = population_size
        self.customers = customers
        self.nv = nv

        self.population = self.initialize_population()

    def initialize_population(self) -> Population:
        initial_solutions = []
        for _ in range(self.population_size):
            remaining_customers = self.customers[:]
            routes = [Route([], self.vehicle_capacity) for _ in range(self.nv)]
            r_index = 0
            while True:
                if len(remaining_customers) == 0:
                    break
                route = routes[r_index]
                customer = random.choice(remaining_customers)
                route.customers.append(customer)
                remaining_customers.remove(customer)
                r_index += 1
                if r_index == self.nv:
                    r_index = 0
            initial_solutions.append(IndividualSolution(routes, self.customers))
        return Population(initial_solutions, self.customers)
