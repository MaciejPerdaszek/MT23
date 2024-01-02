import swarm

last_10 = []


def update_last_10(best_fitness):
    if len(last_10) == 10:
        last_10.pop(0)
    last_10.append(best_fitness)


def run_algorithm(function: (), n_particle: int,
                  x_min: float, x_max: float, y_min: float, y_max: float,
                  inertion_factor: float, cognitive_const: float, social_const: float):
    swarm.fitness_function = function
    particle_params = {
        'x_min': x_min,
        'x_max': x_max,
        'y_min': y_min,
        'y_max': y_max,
        'inertion_factor': inertion_factor,
        'cognitive_const': cognitive_const,
        'social_const': social_const
    }

    s = swarm.generate_swarm(n_particle, particle_params)
    i = 0
    while True:
        swarm.update_swarm(s)
        print('Iteration: ', i, ' best fitness: ', swarm.get_best(s).best_fitness)

        update_last_10(swarm.get_best(s).best_fitness)
        if i > 10:
            if last_10[9] - last_10[0] < 0.000001:
                break
        i += 1

    return swarm.get_best(s)
