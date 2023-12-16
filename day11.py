# Description: Advent of Code - Day 11
import copy

class Universe:
    def __init__(self):
        self.lines = []
        self.galaxies = []
        self.galaxies_chal1 = []
        self.galaxies_chal2 = []
        self.chal1 = 0
        self.chal2 = 0

    def add(self, line):
        self.lines.append(line)

    def finish(self):
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == '#':
                    self.galaxies.append(Galaxy(x, y))

        self.galaxies_chal1 = copy.deepcopy(self.galaxies)
        self.galaxies_chal2 = copy.deepcopy(self.galaxies)

        for y, line in enumerate(self.lines):
            if '#' not in line:
                for galaxy in self.galaxies_chal1:
                    if galaxy.original_y > y:
                        galaxy.expand_vertical(1)

        for x in range(len(self.lines[0])):
            if '#' not in [k[x] for k in self.lines]:
                for galaxy in self.galaxies_chal1:
                    if galaxy.original_x > x:
                        galaxy.expand_horizontal(1)


        for y, line in enumerate(self.lines):
            if '#' not in line:
                for galaxy in self.galaxies_chal2:
                    if galaxy.original_y >= y:
                        galaxy.expand_vertical(999999)

        for x in range(len(self.lines[0])):
            if '#' not in [k[x] for k in self.lines]:
                for galaxy in self.galaxies_chal2:
                    if galaxy.original_x >= x:
                        galaxy.expand_horizontal(999999)

    def challenge1(self):
        for galaxy in self.galaxies_chal1:
            for other in self.galaxies_chal1:
                if galaxy == other:
                    continue
                self.chal1 += galaxy.distance(other)

    def challenge2(self):
        for galaxy in self.galaxies_chal2:
            for other in self.galaxies_chal2:
                if galaxy == other:
                    continue
                self.chal2 += galaxy.distance(other)

    def print_2(self):
        for galaxy in self.galaxies_chal2:
            print(f"{galaxy.original_x}, {galaxy.original_y} -> {galaxy.real_x}, {galaxy.real_y}")


class Galaxy:
    def __init__(self, x, y):
        self.original_x = x
        self.original_y = y
        self.real_x = x
        self.real_y = y
    def expand_vertical(self, by=1):
        self.real_y += by
    def expand_horizontal(self, by=1):
        self.real_x += by
    def distance(self, other):
        return abs(self.real_x - other.real_x) + abs(self.real_y - other.real_y)

if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    u = Universe()
    with open('day11.input', 'r') as f:
        for line in f.readlines():
            u.add(line.strip())
    u.finish()
    u.challenge1()
    u.challenge2()


    print(f"Challenge 1: {int(u.chal1/2)}")
    print(f"Challenge 2: {int(u.chal2/2)}")
