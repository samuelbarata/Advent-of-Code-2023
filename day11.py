# Description: Advent of Code - Day 11

class Universe:
    def __init__(self):
        self.lines = []
        self.galaxies = []

    def add(self, line):
        self.lines.append(line)

    def finish(self):
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == '#':
                    self.galaxies.append(Galaxy(x, y))

        for y, line in enumerate(self.lines):
            if '#' not in line:
                for galaxy in self.galaxies:
                    if galaxy.original_y > y:
                        galaxy.expand_vertical()

        for x in range(len(self.lines[0])):
            if '#' not in [k[x] for k in self.lines]:
                for galaxy in self.galaxies:
                    if galaxy.original_x > x:
                        galaxy.expand_horizontal()

    def challenge(self, increment):
        ret = 0
        for galaxy in self.galaxies:
            for other in self.galaxies:
                if galaxy == other:
                    continue
                ret += galaxy.distance(other, increment)
        return int(ret/2)

class Galaxy:
    def __init__(self, x, y):
        self.original_x = x
        self.original_y = y
        self.expansions_x = 0
        self.expansions_y = 0

    def expand_vertical(self):
        self.expansions_y += 1

    def expand_horizontal(self):
        self.expansions_x += 1

    def distance(self, other, increment=1):
        return  abs((self.original_x + increment*self.expansions_x) - (other.original_x + increment*other.expansions_x)) +\
                abs((self.original_y + increment*self.expansions_y) - (other.original_y + increment*other.expansions_y))

if __name__ == '__main__':
    chal1 = 0
    chal2 = 0
    u = Universe()
    with open('day11.input', 'r') as f:
        for line in f.readlines():
            u.add(line.strip())
    u.finish()

    print(f"Challenge 1: {u.challenge(1)}")
    print(f"Challenge 2: {u.challenge(999999)}")
