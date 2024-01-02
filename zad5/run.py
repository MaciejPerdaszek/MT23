import argparse
import algorithm
from functions import get_function

parser = argparse.ArgumentParser(description='Zadanie 5')
parser.add_argument('-f', '--function', type=int, help='Function number (1-2)')
parser.add_argument('-n', '--n_particle', type=int, help='Number of particles')
parser.add_argument('--inertion_factor', type=float, help='Inertion factor')
parser.add_argument('--cognitive_const', type=float, help='Cognitive constant')
parser.add_argument('--social_const', type=float, help='Social constant')

args = parser.parse_args()

function = get_function(args.function)

result = algorithm.run_algorithm(
            function['func'],
            args.n_particle,
            function['x_min'],
            function['x_max'],
            function['y_min'],
            function['y_max'],
            args.inertion_factor,
            args.cognitive_const,
            args.social_const)

print('Best result: ', round(result.best_fitness, 6), ' x: ', round(result.best_x, 6), ' y: ', round(result.best_y, 6))
