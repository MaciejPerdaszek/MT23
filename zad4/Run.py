import argparse
import Locations
import AntColonyOptimization
import matplotlib.pyplot as plt

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

    print('Best ant path length: ' + str(len(best_ant.visited)))


    def display_best_ant_trail(best_ant_visited):
        plt.figure(figsize=(8, 8))

        for i in range(len(best_ant_visited) - 1):

            location_start = best_ant_visited[i]
            location_end = best_ant_visited[i + 1]

            x_start, y_start = location_start['x'], location_start['y']
            x_end, y_end = location_end['x'], location_end['y']
            if i == 0:
                plt.plot(x_start, y_start, marker='o', color='blue')
            else:
                plt.plot(x_start, y_start, marker='o', color='red')

            plt.plot([x_start, x_end], [y_start, y_end], linestyle='dashed', color='gray')

        last_location = best_ant_visited[-1]
        plt.plot(last_location['x'], last_location['y'], marker='o', color='Blue')

        plt.title('Trail of the best ant in the ant colony algorithm')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')

        plt.savefig('trail.png')

    display_best_ant_trail(best_ant.visited)
