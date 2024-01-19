import random

from zad6.data_structure import Population, Route, Customer, IndividualSolution


class VRPTW:
    def __init__(self, population_size, vehicle_capacity, customers: [Customer]):
        self.vehicle_capacity = vehicle_capacity
        self.population_size = population_size
        self.customers = customers

        self.population = self.initialize_population()

    def initialize_population(self) -> Population:
        initial_solutions = []
        for _ in range(self.population_size):
            remaining_customers = self.customers[:]
            routes_list = []
            while len(remaining_customers) > 0:
                customer_list = []
                load = 0
                while load < self.vehicle_capacity and len(remaining_customers) > 0:
                    customer = random.choice(remaining_customers)
                    if load + customer.demand <= self.vehicle_capacity:
                        customer_list.append(customer)
                        load += customer.demand
                        remaining_customers.remove(customer)
                    else:
                        if all(c.demand + load > self.vehicle_capacity for c in remaining_customers):
                            break
                routes_list.append(Route(customer_list))
            initial_solutions.append(IndividualSolution(routes_list, self.customers))
        return Population(initial_solutions, self.customers)
