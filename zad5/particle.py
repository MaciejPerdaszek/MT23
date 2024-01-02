import math
import random


class Particle:
    def __init__(self, x, y, inertion_factor, cognitive_const, social_const):
        self.x = x
        self.y = y
        self.best_x = x
        self.best_y = y
        self.fitness = float('inf')
        self.best_fitness = float('inf')
        self.inertion_factor = inertion_factor
        self.cognitive_const = cognitive_const
        self.social_const = social_const

        self.velocity_x = 0
        self.velocity_y = 0

    def cognitive_acc(self):
        return self.cognitive_const * random.Random().uniform(0, 1)

    def social_acc(self):
        return self.social_const * random.Random().uniform(0, 1)

    def distance(self):
        return math.sqrt(((self.best_x - self.x) ** 2) + ((self.best_y - self.y) ** 2))

    def cognitive_velocity(self):
        return self.cognitive_acc() * self.distance()

    def social_velocity(self, best_particle):
        return self.social_acc() * best_particle.distance()

    def update_particle(self, best_particle):
        r = random.Random()

        cognitive_acc = self.cognitive_acc()
        cognitive_velocity_x = cognitive_acc * (self.best_x - self.x)
        cognitive_velocity_y = cognitive_acc * (self.best_y - self.y)

        social_acc = self.social_acc()
        social_velocity_x = social_acc * (best_particle.best_x - self.x)
        social_velocity_y = social_acc * (best_particle.best_y - self.y)

        inertion_x = self.inertion_factor * self.velocity_x
        inertion_y = self.inertion_factor * self.velocity_y
        self.velocity_x = inertion_x + cognitive_velocity_x + social_velocity_x
        self.velocity_y = inertion_y + cognitive_velocity_y + social_velocity_y
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y
