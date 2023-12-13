import math


def distance(loc1, loc2):
    return math.sqrt(
        (loc1['x'] - loc2['x']) ** 2
        + (loc1['y'] - loc2['y']) ** 2)


class Locations:
    def __init__(self, file_name):
        self.locations = []
        file = open(file_name, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            o = line.split(' ')
            loc = {'nr': int(o[1]), 'x': int(o[2]), 'y': int(o[3])}
            self.locations.append(loc)
        file.close()

        self.pheromones = self.initiate_pheromones()

    def get_locations(self):
        return self.locations

    def get_pheromones(self):
        return self.pheromones

    def set_pheromones(self, pheromones):
        self.pheromones = pheromones

    def get_pheromone(self, loc1, loc2):
        i = self.locations.index(loc1)
        j = self.locations.index(loc2)
        return self.pheromones[i][j]

    def set_pheromone(self, loc1, loc2, value):
        i = self.locations.index(loc1)
        j = self.locations.index(loc2)
        self.pheromones[i][j] = value

    def initiate_pheromones(self) -> []:
        pheromones = []
        for i in range(len(self.locations)):
            pheromones.append([])
            for j in range(len(self.locations)):
                pheromones[i].append(1)
        return pheromones
