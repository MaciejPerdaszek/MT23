import argparse
import Locations
import AntColonyOptimization

parser = argparse.ArgumentParser(description='Run Ant Colony Optimization program.')
parser.add_argument('-l', '--locations', type=str, help='Path to file with locations data.')
parser.add_argument('-p', '--population-size', type=int, help='Population size.')
parser.add_argument('-i', '--iterations', type=int, help='Number of iterations.')
parser.add_argument('-a', '--alpha', type=float, help='Alpha parameter.')
parser.add_argument('-b', '--beta', type=float, help='Beta parameter.')
parser.add_argument('-e', '--evaporation-rate', type=float, help='Evaporation rate.')
parser.add_argument('-r', '--random-location-probability', type=float, help='Probability of visiting random location.')

args = parser.parse_args()

if (args.locations
        and args.population_size
        and args.iterations
        and args.alpha
        and args.beta
        and args.evaporation_rate
        and args.random_location_probability):
    locations = Locations.Locations(args.locations)
    best_ant = AntColonyOptimization.run(locations, args.population_size, args.iterations, args.alpha, args.beta,
                                         args.evaporation_rate, args.random_location_probability)
    print('Best ant distance: ' + str(best_ant.get_distance()))
    print('Best ant path: ' + str(best_ant.visited))
