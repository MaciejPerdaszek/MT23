import random

from particle import Particle


def fitness_function(x: float, y: float) -> float:  # need to be set by user
    pass


def generate_swarm(n: int, particle_params: dict):
    swarm = []
    r = random.Random()
    for i in range(n):
        swarm.append(Particle(r.uniform(particle_params['x_min'], particle_params['x_max']),
                              r.uniform(particle_params['y_min'], particle_params['y_max']),
                              particle_params['inertion_factor'],
                              particle_params['cognitive_const'],
                              particle_params['social_const']))
    return swarm


def update_fitness(particle: Particle):
    particle.fitness = fitness_function(particle.x, particle.y)
    if particle.fitness < particle.best_fitness:
        particle.best_fitness = particle.fitness
        particle.best_x = particle.x
        particle.best_y = particle.y


def get_best(swarm: list) -> Particle:
    best_particle = swarm[0]
    for particle in swarm:
        if particle.best_fitness < best_particle.best_fitness:
            best_particle = particle
    return best_particle


def update_swarm(swarm: list):
    best_particle = get_best(swarm)
    for particle in swarm:
        particle.update_particle(best_particle)
        update_fitness(particle)
